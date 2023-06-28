import telebot
import logging
import threading
import time
import datetime

import config
import utils
import constants
import functions
import keyboards

logging.basicConfig(level=logging.ERROR, 
                    filename="py_log.log", 
                    filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    )

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


threading.Thread(daemon=True, target=functions.send_unfilled).start()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id,
                   text=config.MENU_MESSAGE,
                   reply_markup=keyboards.main_keyboard(),
                   )


@bot.message_handler(commands=['menu'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id,
                   text=config.MENU_MESSAGE,
                   reply_markup=keyboards.main_keyboard(),
                   )


@bot.callback_query_handler(func = lambda call: True)
def callback_query(call):
    """Handles queries from inline keyboards."""

    # getting message's and user's ids
    message_id = call.message.id
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    user_username = call.from_user.username

    call_data = call.data.split('_')
    query = call_data[0]

    if query == 'service':
        bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=config.SERVICE_MESSAGE,
                            )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.service_keyboard(),
                                    )

    elif query == 'contacts':
        bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=config.CONTACTS_MESSAGE,
                            parse_mode='Markdown',
                            )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.contacts_keyboard(),
                                    )
        
    elif query == 'back':
        destination = call_data[1]

        if destination == 'main':
            bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=config.MENU_MESSAGE,
                            parse_mode='Markdown',
                            )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.main_keyboard(),
                                        )
            
    elif query == 'vcard':
        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        bot.send_contact(chat_id=chat_id,
                     phone_number=config.PHONE_NUMBER,
                     first_name='the-inside',
                     vcard=config.VCARD,
                     )
        bot.send_message(chat_id=chat_id,
                            text=config.CONTACTS_MESSAGE,
                            reply_markup=keyboards.contacts_keyboard(),
                            parse_mode='Markdown',
                            )
    
    elif query == 'type':
        application_type = call_data[1]

        is_type = functions.is_type(user_id)
        
        if is_type:
            functions.update_type(user_id, application_type)
        else:
            functions.add_type(user_id, application_type)


        is_unfilled = functions.is_unfilled_form(user_id, application_type)

        if is_unfilled:
            if not functions.is_spread(user_id, application_type):
                functions.add_info(user_id)

            functions.set_to_none(user_id, application_type)
            unique_id = f'{str(user_id)}_{str(time.time())}'
            functions.update_field(user_id, application_type, 'unique_id', unique_id)
            functions.update_field(user_id, application_type, 'spread', 0)
            start_time = datetime.datetime.utcnow()
            functions.update_field(user_id, application_type, 'start', start_time)

        else:
            functions.add_application(user_id, user_username, application_type)

        bot.edit_message_text(chat_id=chat_id,
                        message_id=message_id,
                        text=config.FORM_MESSAGE,
                        )
    
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.form_keyboard(application_type),
                                    )
        
    elif query == 'form':
        application_type = call_data[1]
        form = constants.ORGANIZATION_FORM[call_data[2]]

        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               application_type,
                               query,
                               form,
                         ),
                         ).start()
        
        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        if form == 'физическое лицо':
            threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               application_type,
                               'organization',
                               '-',
                         ),
                         ).start()
            
            threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               application_type,
                               'position',
                               '-',
                         ),
                         ).start()

            bot.send_message(chat_id=chat_id,
                             text=config.FULL_NAME_PERSON_MESSAGE,
                             reply_markup=keyboards.enter_full_name_person_keyboard(),
                             parse_mode='Markdown',
                             )
        
        else:
            bot.send_message(chat_id=chat_id,
                             text=config.ORGANIZATION_MESSAGE,
                             reply_markup=keyboards.enter_organization_keyboard(),
                             parse_mode='Markdown',
                             )
            
    elif query == 'area':
        area = constants.AREAS[call_data[1]]

        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'telegram',
                               'area',
                               area,
                         ),
                         ).start()
        
        bot.edit_message_text(chat_id=chat_id,
                        message_id=message_id,
                        text=config.INTEGRATION_MESSAGE,
                        parse_mode='Markdown',
                        )
    
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.integration_keyboard(),
                                    )
    
    elif query == 'integration':
        is_needed = int(call_data[1])
        
        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'telegram',
                               'additional',
                               is_needed,
                         ),
                         ).start()
        
        bot.edit_message_text(chat_id=chat_id,
                        message_id=message_id,
                        text=config.PAYMENT_MESSAGE,
                        parse_mode='Markdown',
                        )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.payment_keyboard(),
                                    )
    
    elif query == 'payment':
        is_needed = int(call_data[1])

        application_type = functions.get_type(user_id)

        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               application_type,
                               'payment',
                               is_needed,
                         ),
                         ).start()
        
        if application_type == 'telegram':
            bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=config.ANYQUESTION_MESSAGE,
                            parse_mode='Markdown',
                            )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.question_keyboard(),
                                        )
        
        elif application_type == 'mobile':
            bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=config.TARGET_MESSAGE,
                            parse_mode='Markdown',
                            )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.target_keyboard(),
                                        )
        
        elif application_type == 'web':
            bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=config.ADAPT_MESSAGE,
                            parse_mode='Markdown',
                            )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.adapt_keyboard(),
                                        )
    
    elif query == 'question':
        answer = call_data[1]

        if answer == 'yes':
            try:
                bot.delete_message(chat_id=chat_id, message_id=message_id)
            except:
                pass

            bot.send_message(chat_id=chat_id,
                             text=config.QUESTION_MESSAGE,
                             reply_markup=keyboards.enter_question_keyboard(),
                             parse_mode='Markdown',
                             )
            
        elif answer == 'no':
            functions.handle_text_reply(user_id,
                                '-',
                                'question',
                            )
            
            price = functions.count_price(user_id)
            terms = functions.count_terms(user_id)

            if price:
                price = utils.numbers_format(price)
                reply_text = f'Примерная стоимость вашего проекта: *{price} руб*.\nПримерные сроки написания кода *{terms}* с момента подписания договора.\n\nВаша заявка принята в обработку.'

            else:
                reply_text = 'Расчет стоимости и сроков написания кода на консультации. Заявка принята в работу!\n\nМы с вами свяжемся!'

            bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=reply_text,
                            parse_mode='Markdown',
                            )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.menu_keyboard(),
                                        )

            threading.Thread(daemon=True, 
                            target=functions.add_info,
                            args=(user_id,
                            ),
                            ).start()
            
    elif query == 'menu':
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=message_id,
                                      reply_markup=telebot.types.InlineKeyboardMarkup(),
                                      )
        
        bot.send_message(chat_id=chat_id,
                   text=config.MENU_MESSAGE,
                   reply_markup=keyboards.main_keyboard(),
                   )
    
    elif query == 'platform':
        platform_name = call_data[1]
        difficulty = int(call_data[2])

        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'mobile',
                               'platform',
                               difficulty,
                         ),
                         ).start()
        
        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'mobile',
                               'platform_text',
                               platform_name,
                         ),
                         ).start()

        bot.edit_message_text(chat_id=chat_id,
                        message_id=message_id,
                        text=config.PAYMENT_MESSAGE,
                        parse_mode='Markdown',
                        )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.payment_keyboard(),
                                    )
        
    elif query == 'target':
        target = int(call_data[1])

        if target == 1:
            target_text = 'игры'
        else:
            target_text = 'бизнес' 

        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'mobile',
                               'target',
                               target,
                         ),
                         ).start()
        
        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'mobile',
                               'target_text',
                               target_text,
                         ),
                         ).start()

        bot.edit_message_text(chat_id=chat_id,
                        message_id=message_id,
                        text=config.ANYQUESTION_MESSAGE,
                        parse_mode='Markdown',
                        )
    
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.question_keyboard(),
                                    )
        
    elif query == 'account':
        is_needed = int(call_data[1])

        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'web',
                               'account',
                               is_needed,
                         ),
                         ).start()

        bot.edit_message_text(chat_id=chat_id,
                        message_id=message_id,
                        text=config.PAYMENT_MESSAGE,
                        parse_mode='Markdown',
                        )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.payment_keyboard(),
                                    )
    
    elif query == 'adapt':
        is_needed = int(call_data[1])

        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'web',
                               'adapt',
                               is_needed,
                         ),
                         ).start()
        
        bot.edit_message_text(chat_id=chat_id,
                        message_id=message_id,
                        text=config.ANYQUESTION_MESSAGE,
                        parse_mode='Markdown',
                        )
    
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.question_keyboard(),
                                    )
    
    elif query == 'system':
        system = call_data[1]
        threading.Thread(daemon=True, 
                         target=functions.update_field,
                         args=(user_id,
                               'pk',
                               'system',
                               system,
                         ),
                         ).start()

        bot.edit_message_text(chat_id=chat_id,
                        message_id=message_id,
                        text=config.ANYQUESTION_MESSAGE,
                        parse_mode='Markdown',
                        )
    
        bot.edit_message_reply_markup(chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=keyboards.question_keyboard(),
                                    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    """Handles message with type text."""
    
    if (message.reply_to_message is not None) and\
    (str(message.reply_to_message.from_user.id) == config.BOT_ID):
        
        user_id = message.from_user.id
        chat_id = message.chat.id
        message_id = message.reply_to_message.id

        field = ''
        for keyword in constants.FIELD_TYPE:
            if keyword in message.reply_to_message.text:
                field = constants.FIELD_TYPE[keyword]
                break
        
        if field != '':
            threading.Thread(daemon=True, 
                            target=functions.handle_text_reply,
                            args=(user_id,
                                message.text,
                                field,
                            ),
                            ).start()
            
            try:
                bot.delete_message(chat_id=chat_id, message_id=message_id)
            except:
                pass
            
            if field == 'organization':
                bot.send_message(chat_id=chat_id,
                                text=config.FULL_NAME_RESPONSIBLE_MESSAGE,
                                reply_markup=keyboards.enter_full_name_responsible_keyboard(),
                                parse_mode='Markdown',
                                )
            
            elif field == 'full_name':
                application_type = functions.get_type(user_id)
                legal_form = functions.get_legal_form(user_id, application_type)

                if legal_form == 'физическое лицо':
                    bot.send_message(chat_id=chat_id,
                                text=config.PHONE_MESSAGE,
                                reply_markup=keyboards.enter_phone_keyboard(),
                                parse_mode='Markdown',
                                )
                    
                elif legal_form == 'юридическое лицо':
                    bot.send_message(chat_id=chat_id,
                                text=config.POSITION_MESSAGE,
                                reply_markup=keyboards.enter_position_keyboard(),
                                parse_mode='Markdown',
                                )
            
            elif field == 'position':
                bot.send_message(chat_id=chat_id,
                                text=config.PHONE_MESSAGE,
                                reply_markup=keyboards.enter_phone_keyboard(),
                                parse_mode='Markdown',
                                )
            
            elif field == 'number':
                bot.send_message(chat_id=chat_id,
                                text=config.EMAIL_MESSAGE,
                                reply_markup=keyboards.enter_email_keyboard(),
                                parse_mode='Markdown',
                                )
            
            elif field == 'email':
                bot.send_message(chat_id=chat_id,
                                text=config.AMOUNT_MESSAGE,
                                reply_markup=keyboards.enter_amount_keyboard(),
                                parse_mode='Markdown',
                                )
            
            elif field == 'amount':
                application_type = functions.get_type(user_id)

                if application_type == 'telegram':
                    bot.send_message(chat_id=chat_id,
                                text=config.AREA_MESSAGE,
                                reply_markup=keyboards.area_keyboard(),
                                parse_mode='Markdown',
                                )
                
                elif application_type == 'mobile':
                    bot.send_message(chat_id=chat_id,
                                text=config.PLATFORM_MESSAGE,
                                reply_markup=keyboards.platform_keyboard(),
                                parse_mode='Markdown',
                                )
                
                elif application_type == 'web':
                    bot.send_message(chat_id=chat_id,
                                text=config.ACCOUNT_MESSAGE,
                                reply_markup=keyboards.account_keyboard(),
                                parse_mode='Markdown',
                                )
                
                elif application_type == 'pk':
                    bot.send_message(chat_id=chat_id,
                                text=config.SYSTEM_MESSAGE,
                                reply_markup=keyboards.system_keyboard(),
                                parse_mode='Markdown',
                                )
                    
                elif application_type == 'crm':
                    bot.send_message(chat_id=chat_id,
                        text=config.ANYQUESTION_MESSAGE,
                        reply_markup=keyboards.question_keyboard(),
                        parse_mode='Markdown',
                        )
            
            elif field == 'question':
            
                price = functions.count_price(user_id)
                terms = functions.count_terms(user_id)
                
                if price:
                    price = utils.numbers_format(price)
                    reply_text = f'Примерная стоимость вашего проекта: *{price} руб*.\nПримерные сроки написания кода *{terms}* с момента подписания договора.\n\nВаша заявка принята в обработку.'
                
                else:
                    reply_text = 'Расчет стоимости и сроков написания кода на консультации. Заявка принята в работу!\n\nМы с вами свяжемся!'

                bot.send_message(chat_id=chat_id,
                                text=reply_text,
                                reply_markup=keyboards.menu_keyboard(),
                                parse_mode='Markdown',
                                )

                threading.Thread(daemon=True, 
                                target=functions.add_info,
                                args=(user_id,
                                ),
                                ).start()

        
if __name__ == '__main__':
    # bot.polling(timeout=80)
    while True:
        try:
            bot.polling()
        except:
            pass
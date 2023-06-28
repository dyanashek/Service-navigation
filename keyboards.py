from telebot import types

import config 

def main_keyboard():
    """Generates keyboard that displays in main menu and start message."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Услуги', callback_data = f'service'))
    keyboard.add(types.InlineKeyboardButton('Контакты', callback_data = f'contacts'))
    keyboard.add(types.InlineKeyboardButton('Наш сайт', url = config.SITE_URL))
    return keyboard


def contacts_keyboard():
    """Generates keyboard that displays when user chooses 'contacts' section."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Менеджер в Telegram', url = f'https://t.me/{config.MANAGER_USERNAME}'))
    keyboard.add(types.InlineKeyboardButton('Менеджер Whatsapp', url = f'https://wa.me/{config.MANAGER_WHATSAPP}'))
    keyboard.add(types.InlineKeyboardButton('Карточка контакта', callback_data = 'vcard'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_main'))
    return keyboard


def service_keyboard():
    """Generates keyboard that displays when user chooses 'service' section."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Телеграмм бот', callback_data = 'type_telegram'))
    keyboard.add(types.InlineKeyboardButton('Мобильное приложение', callback_data = 'type_mobile'))
    keyboard.add(types.InlineKeyboardButton('WEB-приложение', callback_data = 'type_web'))
    keyboard.add(types.InlineKeyboardButton('Десктопное приложение', callback_data = 'type_pk'))
    keyboard.add(types.InlineKeyboardButton('CRM системы', callback_data = 'type_crm'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_main'))
    return keyboard


def form_keyboard(application_type):
    """Generates keyboard with organizational legal form."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Физическое лицо', callback_data = f'form_{application_type}_person'))
    keyboard.add(types.InlineKeyboardButton('Юридическое лицо', callback_data = f'form_{application_type}_organization'))
    return keyboard


def enter_organization_keyboard():
    """Makes a reply to a message that asks about organization."""
    return types.ForceReply(input_field_placeholder='Название организации')


def enter_full_name_person_keyboard():
    """Makes a reply to a message that asks about full name."""
    return types.ForceReply(input_field_placeholder='ФИО')


def enter_full_name_responsible_keyboard():
    """Makes a reply to a message that asks about full name of responsible person."""
    return types.ForceReply(input_field_placeholder='ФИО ответственного')


def enter_position_keyboard():
    """Makes a reply to a message that asks about position."""
    return types.ForceReply(input_field_placeholder='Должность')


def enter_phone_keyboard():
    """Makes a reply to a message that asks about phone number."""
    return types.ForceReply(input_field_placeholder='Номер телефона')


def enter_email_keyboard():
    """Makes a reply to a message that asks about email."""
    return types.ForceReply(input_field_placeholder='E-mail')


def enter_amount_keyboard():
    """Makes a reply to a message that asks about users amount."""
    return types.ForceReply(input_field_placeholder='Кол-во пользователей')


def enter_question_keyboard():
    """Makes a reply to a message that asks about question."""
    return types.ForceReply(input_field_placeholder='Ваш вопрос')


def area_keyboard():
    """Generates keyboard with telegram bot usage ares."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Мессенджер', callback_data = 'area_messenger'))
    keyboard.add(types.InlineKeyboardButton('Социальные сети', callback_data = 'area_social'))
    keyboard.add(types.InlineKeyboardButton('Другое', callback_data = 'area_another'))
    return keyboard

def integration_keyboard():
    """Generates keyboard with question about integration of systems."""

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton('✅ Да', callback_data = 'integration_1')
    no = types.InlineKeyboardButton('❌ Нет', callback_data = 'integration_0')
    keyboard.add(yes, no)
    return keyboard

def payment_keyboard():
    """Generates keyboard with question about payments."""

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton('✅ Да', callback_data = 'payment_1')
    no = types.InlineKeyboardButton('❌ Нет', callback_data = 'payment_0')
    keyboard.add(yes, no)
    return keyboard


def account_keyboard():
    """Generates keyboard with question about account."""

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton('✅ Да', callback_data = 'account_1')
    no = types.InlineKeyboardButton('❌ Нет', callback_data = 'account_0')
    keyboard.add(yes, no)
    return keyboard


def adapt_keyboard():
    """Generates keyboard with question about adaptation."""

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton('✅ Да', callback_data = 'adapt_1')
    no = types.InlineKeyboardButton('❌ Нет', callback_data = 'adapt_0')
    keyboard.add(yes, no)
    return keyboard


def question_keyboard():
    """Generates keyboard with question about questions."""

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton('✅ Да', callback_data = 'question_yes')
    no = types.InlineKeyboardButton('❌ Нет', callback_data = 'question_no')
    keyboard.add(yes, no)
    return keyboard


def menu_keyboard():
    """Generates keyboard with menu button."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Меню', callback_data = 'menu'))
    return keyboard

def platform_keyboard():
    """Generates keyboards with platforms."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Android + iOS', callback_data = 'platform_android + ios_1'))
    keyboard.add(types.InlineKeyboardButton('Android', callback_data = 'platform_android_0'))
    keyboard.add(types.InlineKeyboardButton('iOS', callback_data = 'platform_ios_0'))
    return keyboard


def target_keyboard():
    """Generates keyboards with target."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Бизнес', callback_data = 'target_0'))
    keyboard.add(types.InlineKeyboardButton('Игры', callback_data = 'target_1'))
    return keyboard


def system_keyboard():
    """Generates keyboards with systems."""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Microsoft Windows', callback_data = 'system_windows'))
    keyboard.add(types.InlineKeyboardButton('Linux', callback_data = 'system_linux'))
    keyboard.add(types.InlineKeyboardButton('MAC OS', callback_data = 'system_mac os'))
    return keyboard
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# bot's id
BOT_ID = os.getenv('BOT_ID')

# the time in minutes after that unfilled form sends to google sheets
WAIT_TIME = int(os.getenv('WAIT_TIME'))

# manager's username
MANAGER_USERNAME = 'inside235'

# manager's username
MANAGER_WHATSAPP = '79990082846'

# companies phone number
PHONE_NUMBER = '+7 (999) 008 2846'

# companies email
EMAIL = 'alexander@the-inside.info'

# SITE url
SITE_URL = 'https://the-inside.info/'

SPREAD = 'the-inside'
TELEGRAM_SHEET = 'telegram'
MOBILE_SHEET = 'mobile'
WEB_SHEET = 'web'
PK_SHEET = 'pk'
CRM_SHEET = 'crm'

# message that displays with main keyboard
MENU_MESSAGE = 'Выберите интересующий вас раздел:'

# message that displays with service section
SERVICE_MESSAGE = 'Выберите интересующую вас услугу:'

# message with contacts
CONTACTS_MESSAGE = f'''
                    \nНомер телефона:\n*{PHONE_NUMBER}*\
                    \n\
                    \nЭлектронная почта:\n*{EMAIL}*\
                    '''


# contact card
VCARD = f'''BEGIN:VCARD
VERSION:3.0
N:the-inside
ORG:the-inside
TEL;TYPE=work, voice, pref, msg:79990082846
URL:{SITE_URL}
EMAIL;TYPE=INTERNET:{EMAIL}
END:VCARD
'''

FORM_MESSAGE = 'Выберите организационно-правовую форму:'

ORGANIZATION_MESSAGE = 'В ответ на это сообщение пришлите *название вашей компании*.'

FULL_NAME_PERSON_MESSAGE = 'В ответ на это сообщение пришлите ваше *ФИО*.'

FULL_NAME_RESPONSIBLE_MESSAGE = 'В ответ на это сообщение пришлите *ФИО* представителя.'

POSITION_MESSAGE = 'В ответ на это сообщение пришлите *должность* представителя.'

PHONE_MESSAGE = 'В ответ на это сообщение пришлите *контактный номер телефона*.'

EMAIL_MESSAGE = 'В ответ на это сообщение пришлите *адрес электронной почты*.'

AMOUNT_MESSAGE = 'В ответ на это сообщение пришлите *предполагаемое количество пользователей* продукта.'

QUESTION_MESSAGE = 'В ответ на это сообщение задайте любые *вопросы в свободной форме*.'

AREA_MESSAGE = 'Выберите сферу применения бота:'

INTEGRATION_MESSAGE = 'Нужна ли интеграция дополнительных систем?\n\n*(Bitrix24, Amo CRM, Google Аналитика, Яндекс.Метрика и др.)*'

PAYMENT_MESSAGE = 'Необходимо ли подключение эквайринга?'

ANYQUESTION_MESSAGE = 'Есть ли у вас вопросы, которые вы хотели бы задать?'

PLATFORM_MESSAGE = 'Выберите операционную систему:'

TARGET_MESSAGE = 'Укажите назначение приложения:'

ACCOUNT_MESSAGE = 'Необходимо ли создание личного кабинета пользователя?'

ADAPT_MESSAGE = 'Необходима ли адаптация приложения под планшеты, мобильные устройства?'

SYSTEM_MESSAGE = 'Выберите операционную систему:'
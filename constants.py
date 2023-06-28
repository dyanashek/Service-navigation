import gspread

import config

ORGANIZATION_FORM = {
    'person' : 'физическое лицо',
    'organization' : 'юридическое лицо',
}


FIELD_TYPE = {
    'название вашей компании' : 'organization',
    'ФИО' : 'full_name',
    'должность' : 'position', 
    'контактный номер телефона' : 'number',
    'адрес электронной почты' : 'email', 
    'предполагаемое количество пользователей' : 'amount',
    'вопросы в свободной форме' : 'question',
}

AREAS = {
    'messenger' : 'мессенджер',
    'social' : 'социальные сети',
    'another' : 'другое',
}

service_acc = gspread.service_account(filename='service_account.json')
sheet = service_acc.open(config.SPREAD)
SHEETS = {
    'telegram' : sheet.worksheet(config.TELEGRAM_SHEET),
    'mobile' : sheet.worksheet(config.MOBILE_SHEET),
    'web' : sheet.worksheet(config.WEB_SHEET),
    'pk' : sheet.worksheet(config.PK_SHEET),
    'crm' : sheet.worksheet(config.CRM_SHEET),
    }

TELEGRAM_PRICE = {
    0 : 7999,
    1 : 11999,
    2 : 17999,
}

TELEGRAM_TERM = {
    0 : 'от 1 дня',
    1 : 'от 2 дней',
    2 : 'от 3 дней',
}

MOBILE_PRICE = {
    0 : 999999,
    1 : 1199999,
    2 : 1199999,
    3 : 1599999,
}

MOBILE_TERM = {
    0 : 'от 2 месяцев до 5 месяцев',
    1 : 'от 3 месяцев до 7 месяцев',
    2 : 'от 3 месяцев до 7 месяцев',
    3 : 'от 5 месяцев до 12 месяцев',
}

WEB_PRICE = {
    0 : 999999,
    1 : 1199999,
    2 : 1199999,
    3 : 1599999,
}

WEB_TERM = {
    0 : 'от 2 месяцев до 5 месяцев',
    1 : 'от 3 месяцев до 7 месяцев',
    2 : 'от 3 месяцев до 7 месяцев',
    3 : 'от 5 месяцев до 12 месяцев',
}

LAST_COLUMN = {
    'telegram' : 'O',
    'mobile' : 'O',
    'web' : 'O',
    'pk' : 'M',
    'crm' : 'L',
    }
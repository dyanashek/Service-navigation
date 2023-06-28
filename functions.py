import sqlite3
import logging
import inspect
import datetime
import time
import itertools

import utils
import constants
import config

def add_application(user_id, user_username, application_type):
    '''Adds a new application to one of the tables (depends on type).'''

    database = sqlite3.connect("inside.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = database.cursor()

    unique_id = f'{str(user_id)}_{str(time.time())}'
    start_time = datetime.datetime.utcnow()

    cursor.execute(f'''
            INSERT INTO {application_type} (unique_id, user_id, username, start)
            VALUES ("{unique_id}", "{user_id}", "{user_username}", "{start_time}")
            ''')

    database.commit()
    cursor.close()
    database.close()

    logging.info(f'{inspect.currentframe().f_code.co_name}: Добавлен пользователь {user_id} в {application_type}.')


def is_unfilled_form(user_id, application_type):
    """Checks if user has unfilled form. 
    Returns False if the user didn't.
    """

    database = sqlite3.connect("inside.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = database.cursor()

    user = cursor.execute(f"SELECT * FROM {application_type} WHERE user_id='{user_id}'").fetchall()

    cursor.close()
    database.close()

    if user != []:
        user = user[0]
        return user
    
    return False


def is_type(user_id):
    """Checks if user already has an application type. 
    Returns False if doesn't.
    """

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    user = cursor.execute(f"SELECT type FROM users WHERE user_id='{user_id}'").fetchall()

    cursor.close()
    database.close()

    if user != []:
        user = user[0]
        return user
    
    return False


def set_to_none(user_id, application_type):
    """Sets all filled fields to None in unfilled application."""

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    if application_type == 'telegram':
        cursor.execute(f'''UPDATE {application_type}
                        SET form=NULL, organization=NULL, full_name=NULL, 
                        position=NULL, number=NULL, email=NULL, area=NULL,
                        amount=NULL, additional=NULL, payment=NULL, question=NULL,
                        date=NULL
                        WHERE user_id="{user_id}"
                        ''')
    
    elif application_type == 'mobile':
        cursor.execute(f'''UPDATE {application_type}
                        SET form=NULL, organization=NULL, full_name=NULL, 
                        position=NULL, number=NULL, email=NULL, amount=NULL,
                        platform=NULL, platform_text=NULL, payment=NULL, target=NULL,
                        target_text=NULL, question=NULL, date=NULL
                        WHERE user_id="{user_id}"
                        ''')

    elif application_type == 'web':
        cursor.execute(f'''UPDATE {application_type}
                        SET form=NULL, organization=NULL, full_name=NULL, 
                        position=NULL, number=NULL, email=NULL, amount=NULL,
                        account=NULL, payment=NULL, adapt=NULL, question=NULL, 
                        date=NULL
                        WHERE user_id="{user_id}"
                        ''')
        
    database.commit()
    cursor.close()
    database.close()

    logging.info(f'{inspect.currentframe().f_code.co_name}: Сброшены заполненные поля пользователя {user_id} в {application_type}.')


def add_type(user_id, application_type):
    """Sets a new type of application for user who doesn't have one already."""

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    cursor.execute(f'''
            INSERT INTO users (user_id, type)
            VALUES ("{user_id}", "{application_type}")
            ''')

    database.commit()
    cursor.close()
    database.close()

    logging.info(f'{inspect.currentframe().f_code.co_name}: Для пользователя {user_id} добавлен тип: {application_type}.')


def update_type(user_id, application_type):
    """Sets a new type of application for user who already has one."""

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    cursor.execute(f'''UPDATE users
                    SET type="{application_type}"
                    WHERE user_id="{user_id}"
                    ''')

    database.commit()
    cursor.close()
    database.close()

    logging.info(f'{inspect.currentframe().f_code.co_name}: Для пользователя {user_id} обновлен тип: {application_type}.')


def update_field(user_id, application_type, field, value):
    """Sets a new value to a field."""

    database = sqlite3.connect("inside.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = database.cursor()

    cursor.execute(f'''UPDATE {application_type}
                    SET {field}=?
                    WHERE user_id="{user_id}"
                    ''', (value,))

    database.commit()
    cursor.close()
    database.close()


def get_legal_form(user_id, application_type):
    """Gets users legal form."""

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    form = cursor.execute(f"SELECT form FROM {application_type} WHERE user_id='{user_id}'").fetchall()[0][0]

    cursor.close()
    database.close()

    return form


def get_type(user_id):
    """Gets users application type."""

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    application_type = cursor.execute(f"SELECT type FROM users WHERE user_id='{user_id}'").fetchall()[0][0]

    cursor.close()
    database.close()

    return application_type

def handle_text_reply(user_id, value, field):
    """Indicates the application type of user and updates field."""

    application_type = get_type(user_id)
    update_field(user_id, application_type, field, value)


def count_price(user_id):
    """Depends on users choices counts the product cost."""

    application_type = get_type(user_id)

    if application_type == 'telegram':
        cost_factors = telegram_cost_factors(user_id)
        cost = constants.TELEGRAM_PRICE[cost_factors]

    elif application_type == 'mobile':
        cost_factors = mobile_cost_factors(user_id)
        cost = constants.MOBILE_PRICE[cost_factors]

    elif application_type == 'web':
        cost_factors = web_cost_factors(user_id)
        cost = constants.WEB_PRICE[cost_factors]

    else:
        cost = False

    return cost


def count_terms(user_id):
    """Depends on users choices select terms."""

    application_type = get_type(user_id)

    if application_type == 'telegram':
        terms_factors = telegram_cost_factors(user_id)
        terms = constants.TELEGRAM_TERM[terms_factors]

    elif application_type == 'mobile':
        terms_factors = mobile_cost_factors(user_id)
        terms = constants.MOBILE_TERM[terms_factors]

    elif application_type == 'web':
        terms_factors = web_cost_factors(user_id)
        terms = constants.WEB_TERM[terms_factors]

    else:
        terms = False

    return terms


def telegram_cost_factors(user_id):
    """Summarize telegrams cost factors"""

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    cost_factors = cursor.execute(f"SELECT additional, payment FROM telegram WHERE user_id='{user_id}'").fetchall()[0]

    cursor.close()
    database.close()

    return sum(cost_factors)


def mobile_cost_factors(user_id):
    """Summarize mobile cost factors"""

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    cost_factors = cursor.execute(f"SELECT platform, payment, target FROM mobile WHERE user_id='{user_id}'").fetchall()[0]

    cursor.close()
    database.close()

    return sum(cost_factors)


def web_cost_factors(user_id):
    """Summarize web cost factors"""

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    cost_factors = cursor.execute(f"SELECT account, payment, adapt FROM web WHERE user_id='{user_id}'").fetchall()[0]

    cursor.close()
    database.close()

    return sum(cost_factors)


def to_google_sheets(application_info, application_type):
    """Adds information that user filled to google sheets."""

    work_sheet = constants.SHEETS[application_type]
    row = empty_row(application_type, application_info[0])
    last_column = constants.LAST_COLUMN[application_type]
    
    try:
        work_sheet.update(f'A{row}:{last_column}{row}', [application_info])
        update_field(application_info[1], application_type, 'spread', 1)
    except Exception as ex:
        pass
    
    logging.info(f'{inspect.currentframe().f_code.co_name}: Данные добавлены в таблицу {application_type}.')


def add_info(user_id):
    """Collects information that user filled, validate it and adds to google sheets."""

    application_type = get_type(user_id)
    date_today = (datetime.datetime.utcnow() + datetime.timedelta(hours=3)).date()
    update_field(user_id, application_type, 'date', date_today)
    application_info = is_unfilled_form(user_id, application_type)
    application_info = utils.format_info(application_info, application_type)
    to_google_sheets(application_info, application_type)

def empty_row(application_type, unique_id):
    """Gets the number of first empty row in table."""

    work_sheet = constants.SHEETS[application_type]
    col_values = work_sheet.col_values(1)
    if unique_id in col_values:
        row = col_values.index(unique_id) + 1
    else:
        row = len(col_values) + 1

    return row


def send_unfilled():
    '''Sends unfilled forms to google sheets after a period of time.'''

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    while True:
        time_filter = datetime.datetime.utcnow() - datetime.timedelta(minutes=config.WAIT_TIME)

        ids = cursor.execute(f"SELECT user_id FROM telegram WHERE spread=0 and start<'{time_filter}'").fetchall()
        if ids:
            ids = itertools.chain.from_iterable(ids)

            for user_id in ids:
                try:
                    add_unfilled_info(user_id, 'telegram')
                except:
                    pass
        
        ids = cursor.execute(f"SELECT user_id FROM mobile WHERE spread=0 and start<'{time_filter}'").fetchall()
        if ids:
            ids = itertools.chain.from_iterable(ids)

            for user_id in ids:
                try:
                    add_unfilled_info(user_id, 'mobile')
                except:
                    pass

        ids = cursor.execute(f"SELECT user_id FROM web WHERE spread=0 and start<'{time_filter}'").fetchall()
        if ids:
            ids = itertools.chain.from_iterable(ids)

            for user_id in ids:
                try:
                    add_unfilled_info(user_id, 'web')
                except:
                    pass
        
        ids = cursor.execute(f"SELECT user_id FROM pk WHERE spread=0 and start<'{time_filter}'").fetchall()
        if ids:
            ids = itertools.chain.from_iterable(ids)

            for user_id in ids:
                try:
                    add_unfilled_info(user_id, 'pk')
                except:
                    pass
        
        ids = cursor.execute(f"SELECT user_id FROM crm WHERE spread=0 and start<'{time_filter}'").fetchall()
        if ids:
            ids = itertools.chain.from_iterable(ids)

            for user_id in ids:
                try:
                    add_unfilled_info(user_id, 'crm')
                except:
                    pass
        
        time.sleep(1)
        
    
def is_spread(user_id, application_type):
    ''''''

    database = sqlite3.connect("inside.db")
    cursor = database.cursor()

    try:
        user_id = cursor.execute(f"SELECT spread FROM {application_type} WHERE user_id='{user_id}'").fetchall()[0][0]
    except:
        return False
    
    if user_id == 1:
        return True

    return False


def add_unfilled_info(user_id, application_type):
    """Collects information that user filled, validate it and adds to google sheets."""

    date_today = (datetime.datetime.utcnow() + datetime.timedelta(hours=3)).date()
    update_field(user_id, application_type, 'date', date_today)
    application_info = is_unfilled_form(user_id, application_type)
    application_info = utils.format_info(application_info, application_type)
    to_google_sheets(application_info, application_type)
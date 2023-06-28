import sqlite3
import logging

database = sqlite3.connect("inside.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = database.cursor()

try:
    # creates table for telegram bot orders
    cursor.execute('''CREATE TABLE telegram (
        id INTEGER PRIMARY KEY,
        unique_id VARCHAR (50),
        user_id VARCHAR (30),
        username VARCHAR (30),
        form VARCHAR (30),
        organization VARCHAR (30),
        full_name VARCHAR (80),
        position VARCHAR (50),
        number VARCHAR (20),
        email VARCHAR (30),
        area TEXT,
        amount INTEGER,
        additional BOOLEAN,
        payment BOOLEAN,
        question TEXT,
        date DATE,
        spread BOOLEAN DEFAULT False,
        start TIMESTAMP
    )''')
except:
    logging.error('Telegram table already exists.')

try:
    # creates table for mobile orders
    cursor.execute('''CREATE TABLE mobile (
        id INTEGER PRIMARY KEY,
        unique_id VARCHAR (50),
        user_id VARCHAR (30),
        username VARCHAR (30),
        form VARCHAR (30),
        organization VARCHAR (30),
        full_name VARCHAR (80),
        position VARCHAR (50),
        number VARCHAR (20),
        email VARCHAR (30),
        amount INTEGER,
        platform BOOLEAN,
        platform_text VARCHAR (15),
        payment BOOLEAN,
        target BOOLEAN,
        target_text VARCHAR (10),
        question TEXT,
        date DATE,
        spread BOOLEAN DEFAULT False,
        start TIMESTAMP
    )''')
except:
    logging.error('Mobile table already exists.')

try:
    # creates table for web orders
    cursor.execute('''CREATE TABLE web (
        id INTEGER PRIMARY KEY,
        unique_id VARCHAR (50),
        user_id VARCHAR (30),
        username VARCHAR (30),
        form VARCHAR (30),
        organization VARCHAR (30),
        full_name VARCHAR (80),
        position VARCHAR (50),
        number VARCHAR (20),
        email VARCHAR (30),
        amount INTEGER,
        account BOOLEAN,
        payment BOOLEAN,
        adapt BOOLEAN,
        question TEXT,
        date DATE,
        spread BOOLEAN DEFAULT False,
        start TIMESTAMP
    )''')
except:
    logging.error('Web table already exists.')

try:
    # creates table for pk orders
    cursor.execute('''CREATE TABLE pk (
        id INTEGER PRIMARY KEY,
        unique_id VARCHAR (50),
        user_id VARCHAR (30),
        username VARCHAR (30),
        form VARCHAR (30),
        organization VARCHAR (30),
        full_name VARCHAR (80),
        position VARCHAR (50),
        number VARCHAR (20),
        email VARCHAR (30),
        amount INTEGER,
        system VARCHAR (10),
        question TEXT,
        date DATE,
        spread BOOLEAN DEFAULT False,
        start TIMESTAMP
    )''')
except:
    logging.error('Pk table already exists.')

try:
    # creates table for crm orders
    cursor.execute('''CREATE TABLE crm (
        id INTEGER PRIMARY KEY,
        unique_id VARCHAR (50),
        user_id VARCHAR (30),
        username VARCHAR (30),
        form VARCHAR (30),
        organization VARCHAR (30),
        full_name VARCHAR (80),
        position VARCHAR (50),
        number VARCHAR (20),
        email VARCHAR (30),
        amount INTEGER,
        question TEXT,
        date DATE,
        spread BOOLEAN DEFAULT False,
        start TIMESTAMP
    )''')
except Exception as ex:
    logging.error(f'Crm table already exists. {ex}')

try:
    # creates table for telegram bot orders
    cursor.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        user_id VARCHAR (30),
        type VARCHAR (30)
    )''')
except:
    logging.error('Users table already exists.')


# cursor.execute("DELETE FROM crm WHERE id<>10000")
# database.commit()
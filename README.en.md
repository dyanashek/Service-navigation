# Collect applications bot
## Изменить язык: [Русский](README.md)
***
Transfers user responses to a Google spreadsheet. Provides a brief introduction to the company.
## [DEMO](README.demo.md)
## Commands:
**For convenience, it is recommended to add these commands to the side menu of the bot using [BotFather](https://t.me/BotFather).**
- menu - calls the menu

## Installation and use:
- error logging is done in the py_log.log file
- create and activate virtual environment (if necessary):
```sh
python3 -m venv venv
source venv/bin/activate # for mac
source venv/Scripts/activate # for windows
```
- Install dependencies:
```sh
pip install -r requirements.txt
```
- in the .env file specify:\
Bot telegram token: **TELEBOT_TOKEN**=TOKEN\
Bot ID: **BOT_ID**=ID (first digits from bot token, before :)\
Time in minutes after which an incomplete application is sent to google sheets: **WAIT_TIME**=15
- get file with credential (connection parameters):\
https://console.cloud.google.com/ \
https://www.youtube.com/watch?v=bu5wXjz2KvU - instruction from 00:00 to 02:35\
Save the resulting file in the root of the project, with the name **service_account.json**
- provide service e-mail with access to the table (instruction in the video at the link above)
- set the appropriate names for the table and sheets in google sheets, the names of the variables with the names of the tables in the config.py file are in brackets:\
Table name - **the-inside** (SPREAD)\
The name of the sheet with requests for Telegram bots is **telegram** (TELEGRAM_SHEET)\
The name of the sheet with applications for mobile applications is **mobile** (MOBILE_SHEET)\
The name of the sheet with applications for web applications is **web** (WEB_SHEET)\
The name of the sheet with requests for desktop applications is **pk** (PK_SHEET)\
The name of the sheet with applications for the CRM system - **crm** (CRM_SHEET)
- run the project:
```sh
python3 main.py
```
## Recommendations for use:
- before activating the bot, it is recommended to set column names for easy navigation:
     - the order of information displayed on the sheet with applications for telegram bots:
         1. unique ticket ID
         2. user id in telegram
         3. username of the user in telegram
         4. legal person / individual face
         5. name of the organization (if an individual, automatically put "-")
         6. Name
         7. position (if an individual, automatically put "-")
         8. phone number
         9. email
         10. scope of the bot
         11. estimated number of users
         12. the need for additional systems (Bitrix, Amo crm, etc.)
         13. the need to connect acquiring
         14. additional questions ("-" in the absence)
         15. date of completion of filling out the application (Moscow time utc +3)

     - the order of displayed information on the sheet with applications for mobile applications:
         1. unique ticket ID
         2. user id in telegram
         3. username of the user in telegram
         4. legal person / individual face
         5. name of the organization (if an individual, automatically put "-")
         6. Name
         7. position (if an individual, automatically put "-")
         8. phone number
         9. email
         10. estimated number of users
         11. development platform
         12. the need to connect acquiring
         13. Scope of application (business / games)
         14. additional questions ("-" in the absence)
         15. date of completion of filling out the application (Moscow time utc +3)

     - the order of the displayed information on the sheet with applications for web applications:
         1. unique ticket ID
         2. user id in telegram
         3. username of the user in telegram
         4. legal person / individual face
         5. name of the organization (if an individual, automatically put "-")
         6. Name
         7. position (if an individual, automatically put "-")
         8. phone number
         9. email
         10. estimated number of users
         11. the need to develop a personal account
         12. the need to connect acquiring
         13. the need for adaptation for mobile devices
         14. additional questions ("-" in the absence)
         15. date of completion of filling out the application (Moscow time utc +3)

     - the order of displayed information on the sheet with applications for desktop applications:
         1. unique ticket ID
         2. user id in telegram
         3. username of the user in telegram
         4. legal person / individual face
         5. name of the organization (if an individual, automatically put "-")
         6. Name
         7. position (if an individual, automatically put "-")
         8. phone number
         9. email
         10. estimated number of users
         11. operating system
         12. additional questions ("-" in the absence)
         13. date of completion of filling out the application (Moscow time utc +3)

     - the order of information displayed on the sheet with applications for the crm system:
         1. unique ticket ID
         2. user id in telegram
         3. username of the user in telegram
         4. legal person / individual face
         5. name of the organization (if an individual, automatically put "-")
         6. Name
         7. position (if an individual, automatically put "-")
         8. phone number
         9. email
         10. estimated number of users
         11. additional questions ("-" in the absence)
         12. date of completion of filling out the application (Moscow time utc +3)

- the bot starts filling from the first empty line (the check is carried out on column A) - do not leave this column empty at the top of the table
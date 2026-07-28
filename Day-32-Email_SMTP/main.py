import datetime as dt
import smtplib
import random
import pandas as pd
TODAY = (7,28)
MY_EMAIL = "db9695733@gmail.com"
MY_PASSWORD = "zxlkdltjlglbsjij"

today = dt.datetime.today()

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month , data_row.day ):data_row for (index , data_row ) in data.iterrows()}

if TODAY in birthdays_dict:
    birthday_person = birthdays_dict[TODAY]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file :
        contents = letter_file.read()
        contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",465) as connection:
        connection.starttls()
        connection.login(MY_EMAIL , MY_PASSWORD)





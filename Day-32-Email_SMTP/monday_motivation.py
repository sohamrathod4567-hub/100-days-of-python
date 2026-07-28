import smtplib
import datetime as dt
import random

my_email = "db9695733@gmail.com"
password = "zxlkdltjlglbsjij"

with open("quotes.txt", "r") as file :
    data = file.readlines()

one_quote = random.choice(data)

def send_mail():
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email, to_addrs="rathodsoham999@gmail.com", msg=f"Subject: Monday Motivation\n\n{one_quote} ")
    print("Mail sent successfully")
weekday = dt.datetime.today().weekday()
print(weekday)

if weekday == 1 :
    send_mail()

import os
import smtplib
from dotenv import load_dotenv
from data_manager import DataManager
load_dotenv()
EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_PASSWORD")
USER = DataManager().get_customer_emails()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
   def __init__(self,content):
        body = "\n".join(content)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=USER,
                                    msg=f"Subject:Cheap Flight NotiFication \n \n  {body}"
                                    )
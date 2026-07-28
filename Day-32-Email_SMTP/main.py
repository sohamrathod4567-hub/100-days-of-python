import smtplib

my_email = "db9695733@gmail.com"
password = "zxlkdltjlglbsjij"

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password= password)
    connection.sendmail(from_addr=my_email, to_addrs="rathodsoham999@gmail.com", msg="Subject: popli\n\nello bonjour")












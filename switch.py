from twilio.rest import Client
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

client = Client('ACaaebe8c489801a9f8f302a0bbc25f1ec', 'f51e489628ba64e7f77af266c023bf8e')

def death_text(to_number, content):
    client.messages.create(to=to_number, from_="+12054797696", body=content)

def email_send(SentTo, Content, Subject):
    sender_address = "deadmansswitcher@gmail.com"
    sender_pass = "76pM?JaaaEU7``(j"
    receiver_address = SentTo
    mail_content = Content
    # Setup the MIME
    message = MIMEMultipart()
    message["From"] = sender_address
    message["To"] = receiver_address
    message["Subject"] = Subject  # The subject line
    message.attach(MIMEText(mail_content, "plain"))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("Email Sent")

death_reminder = "Verify you're alive. NOW! http://99.108.71.191:443"
emailcontent = "You still alive? http://99.108.71.191:443"
panicmode = "Verify you're alive. Things are gonna get bad soon. http://99.108.71.191:443"

# Sending a Reminder to verify life
def livetest():
    email_send("mindersteve@protonmail.com", emailcontent, "LivingTest")
    print("work")

schedule.every().monday.at("09:00").do(livetest)

#Assuming death 
def deathwrite():
    file = open('deadoralive.txt', 'w')
    file.write('dead')

schedule.every().monday.at("05:00").do(deathwrite)

def verifyalive():
    file = open('deadoralive.txt', 'r')
    status = file.read()
    print(status) 
    if status == "dead": 
        email_send("mindersteve@protonmail.com", panicmode, "VERIFY")
        death_text("+12058642045", death_reminder)
        email_send("aidendombrosky@gmail.com", panicmode, "VERIFY")
        email_send("aidendombrosky05@gmail.com", panicmode, "VERIFY")
        email_send("1967183763@hcs-students.net", panicmode, "VERIFY")

def finalverifyalive():
    file = open('deadoralive.txt', 'r')
    status = file.read()
    print(status) 
    if status == "dead": 
        email_send("mindersteve@protonmail.com", panicmode, "VERIFY")
        death_text("+12058642045", death_reminder)
        email_send("aidendombrosky@gmail.com", panicmode, "VERIFY")
        email_send("aidendombrosky05@gmail.com", panicmode, "VERIFY")
        email_send("1967183763@hcs-students.net", panicmode, "VERIFY")
        file = open('deadoralive.txt', 'w')
        file.write('deaddead')
schedule.every().wednesday.at("12:00").do(verifyalive)
schedule.every().thursday.at("12:00").do(verifyalive)
schedule.every().friday.at("12:00").do(verifyalive)
schedule.every().saturday.at("12:00").do(finalverifyalive)
while True:
   #Checks whether a scheduled task
   #is pending to run or not
    schedule.run_pending()
    time.sleep(1)

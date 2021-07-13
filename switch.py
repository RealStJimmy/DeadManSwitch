from twilio.rest import Client
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

client = Client('Client Data', 'Client Data ')

def death_text(to_number, content):
    client.messages.create(to=to_number, from_="+12054797696", body=content)

def email_send(SentTo, Content, Subject):
    sender_address = "deadmansswitcher@gmail.com"
    sender_pass = "Pass"
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

death_reminder = "Verify message"
emailcontent = "Verify message"
panicmode = "Verify message "

# Sending a Reminder to verify life
def livetest():
    email_send("emailplaceholder@protonmail.com", emailcontent, "LivingTest")
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
        email_send("placeholder", panicmode, "VERIFY")
        death_text("+placeholder", death_reminder)
        email_send("placeholder", panicmode, "VERIFY")
        email_send("placeholder", panicmode, "VERIFY")
        email_send("placeholder", panicmode, "VERIFY")

def finalverifyalive():
    file = open('deadoralive.txt', 'r')
    status = file.read()
    print(status) 
    if status == "dead": 
        email_send("placeholder", panicmode, "VERIFY")
        death_text("+placeholder", death_reminder)
        email_send("placeholder", panicmode, "VERIFY")
        email_send("placeholder", panicmode, "VERIFY")
        email_send("placeholder", panicmode, "VERIFY")
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

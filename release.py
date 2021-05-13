import schedule
import time
from twilio.rest import Client

client = Client('ACaaebe8c489801a9f8f302a0bbc25f1ec', 'f51e489628ba64e7f77af266c023bf8e')

def releaseall(to_number, content):
    file = open('deadoralive.txt', 'r')
    status = file.read()
    print(status) 
    if status == "deaddead": 
        client.messages.create(to=to_number, from_="+12054797696", body=content)


schedule.every().sunday.at("23:59").do(releaseall)

while True:
   #Checks whether a scheduled task
   #is pending to run or not
    schedule.run_pending()
    time.sleep(1)
import schedule
import time
from twilio.rest import Client

client = Client('ACaaebe8c489801a9f8f302a0bbc25f1ec', 'f51e489628ba64e7f77af266c023bf8e')

content = '''
If you're reciving this, Aiden Dombrosky is dead.\n
Now don't panic, it's entirely possible he's just really shitty at writing code and that he's still alive.\n 
Or that he's on vacation and forgot to turn off the system\n
Go to this site for his last message to you.\n 
If you know he's alive please don't go here\n
http://99.108.71.191:443/M2PMavToIbuJutmknngE
'''



def releaseall():
    file = open('deadoralive.txt', 'r')
    status = file.read()
    print(status) 
    if status == "deaddead": 
        client.messages.create(to="+12058642045", from_="+12054797696", body=content)
        client.messages.create(to="+12056009541", from_="+12054797696", body=content)
        client.messages.create(to="+12055426123", from_="+12054797696", body=content)
        client.messages.create(to="+12057578890", from_="+12054797696", body=content)
        client.messages.create(to="+12057197187", from_="+12054797696", body=content)
        client.messages.create(to="+12058877999", from_="+12054797696", body=content)

schedule.every().sunday.at("23:30").do(releaseall)

while True:
   #Checks whether a scheduled task
   #is pending to run or not
    schedule.run_pending()
    time.sleep(1)

import schedule
import time
from twilio.rest import Client

client = Client('Client Data', 'Client Data')

content = '''
PLACEHOLDER FOR RELASE INFOR 
Website placeholder 
'''



def releaseall():
    file = open('deadoralive.txt', 'r')
    status = file.read()
    print(status) 
    if status == "deaddead": 
        client.messages.create(to="+NumberPlaceHolder", from_="+NumberPlaceholder", body=content)


schedule.every().sunday.at("23:30").do(releaseall)

while True:
   #Checks whether a scheduled task
   #is pending to run or not
    schedule.run_pending()
    time.sleep(1)

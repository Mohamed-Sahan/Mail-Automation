#importing essential library files.

import datetime as dt
import time
import smtplib
import json

def send_email():
    with open(r"C:\Users\91948\Downloads\json sample.json")as f:   #file's path
        data=json.load(f)
        gmailaddress = 'sender id'
        gmailpassword = 'password'
        mailto = data['email_ids'] #importing maild ids froms json 
        SUBJECT='SD TEAM 5'
        msg=data['content'] #importing mail content from json
        message = 'Subject: {}\n\n{}'.format(SUBJECT, msg)
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, mailto , message)
        mailServer.quit()

def send_email_at(send_time):
    send_email()
    print('email sent')
    time.sleep(60*120) #(seconds*minutes)
    
#setting date and time in 24hrs format(yyyy,mm,dd,%H,%M,%S)
first_email_time = dt.datetime(2021,06,15,20,19,0)  
interval = dt.timedelta(minutes=0) 

send_time = first_email_time
while True:
    send_time = send_time + interval
    send_email_at(send_time)

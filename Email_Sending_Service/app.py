from flask import Flask, redirect, url_for, request
from flask import request
import threading
import multiprocessing
from multiprocessing import Process
import os
import time
import requests
import Email_Sender
from flask import Flask, render_template


email_address=[]   #this list will contain all email ids provided by user
schedule_time=[]   #this list will contain schedule time given by user

def schedule_email_job():
    
    #function to convert time into 24 hours format
    def convert_to_24(str1):

    # Checking if last two elements of time is AM and first two elements are 12
        if str1[-2:] == "AM" and str1[:2] == "12":
            return "00" + str1[2:-2]

    # remove the AM
        elif str1[-2:] == "AM":
            return str1[:-3]

    # Checking if last two elements of time is PM and first two elements are 12
        elif str1[-2:] == "PM" and str1[:2] == "12":
            return str1[:-2]

        else:

        # add 12 to hours and remove PM
            return str(int(str1[:2]) + 12) + str1[2:5]
        
    while(1):
    #if current time is equal to scheduled time send email to all recipients
        if len(schedule_time)>=1:
            cur_sys_time=time.strftime("%H:%M") # Get current system time it will be in 24 hours format
            
            usr_time=convert_to_24(schedule_time[len(schedule_time)-1]) #convert user provided time into 24 hours format  
            
            #iterate through all emaid id's and send query result to corresponding email id if scheduled time==system time
            if cur_sys_time==usr_time:
                for i in email_address:
                    Email_Sender.fun_email(i)   
                time.sleep(50000) #sleep it for atleast 12 hours because i have to send email once in a day

app = Flask(__name__)

@app.route('/home')
def home():
    
    return render_template('first.html')  #render first.html page 

#it is  route to get value of email id and schedule time from user we are using GET and POST http methods
@app.route('/anand',methods = ['POST', 'GET'])

def login():
   if request.method == 'POST':
       if 'email_id' in request.form.keys():
           email_address.append(request.form['email_id']) #append email id to email_address list 
           return render_template("first.html")  #render first.html page to take another input from user
       else:
           schedule_time.append(str(request.form['sch_time']))   #append schedule time to schedule_time list 
           return render_template("first.html")

if __name__ == '__main__':
    #create a thread set target job=schedule_email_job this thread will run in background
    threading.Thread(target=schedule_email_job).start()
    
    #run flask server at port 5001 you can access it by typing localhost:5001/home in browser
    app.run(debug = True,port=5001)

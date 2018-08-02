import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
def fun_email(reciever_email_id):
    fromaddr = "redashproject123@gmail.com"
    toaddr = reciever_email_id
    msg = MIMEMultipart()
    msg['From'] = fromaddr
 
    msg['To'] = toaddr

    #subject of email
    msg['Subject'] = "Redash Query Result"

    body = "Query Result"

    msg.attach(MIMEText(body, 'plain'))
    
    #Query url to download result in csv format
    query_url = "http://localhost/api/queries/2/results.csv?api_key=7KzXLNM9bWJa776YjBgXdG1FnQlmMLDJ1hLb87c1"
    r = requests.get(query_url) #Get response from requested url

    #create a file name Query_Result.csv and append contents of results into it
    with open("Query_Result.csv",'wb') as f:
        f.write(r.content)

    f.close() 

    filename = "Query_Result.csv"
    attachment = open("Query_Result.csv", "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, "redash@123")

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()
    os.remove("Query_Result.csv")

#!/usr/bin/env python3
import smtplib
import ssl

port = 465 #SSL
context = ssl.create_default_context()
password = "123"
message = """\
    Subject: Message
    
    Hello!""" 
reciever = "americaamerica305@gmail.com"

#send email
with smtplib.SMTP_SSL("smtp@gmail.com", port, context) as server:
    server.login("borna.santavec124@gmail.com", password)
    server.sendmail("borna.santavec124@gmail.com", reciever)
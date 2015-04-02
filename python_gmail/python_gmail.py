#! /usr/bin/python

import smtplib

FROM = "robot.mailer.deamon@gmail.com"
TO = FROM
SUBJECT = "Test Email"
BODY = "<B>Test</B>"

# The below code never changes, though obviously those variables need values.
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login(FROM, "PASSWORD")

# Send an email from the GMail account
headers = "\r\n".join(["from: " + FROM,
                       "subject: " + SUBJECT,
                       "to: " + TO,
                       "mime-version: 1.0",
                       "content-type: text/html"])

# body_of_email can be plaintext or html!                    
content = headers + "\r\n\r\n" +  BODY
session.sendmail(FROM, TO, content)
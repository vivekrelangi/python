"""import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('wepdet@gmail.com','We@#demo0987')

server.sendmail('indobot@gmail.com','indobot@gmail.com','Mail sent from python code')
print('Mail sent')"""
from email.message import EmailMessage
#from maildm import password
import ssl
import smtplib

email_sender = 'wepdet@gmail.com'
email_password = 'qywd szyo upne ymsd'

email_receiver = 'tewagas520@iliken.com'

subject = "Mail from python code"
body="""Sample body msg."""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

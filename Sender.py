import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465

sender = 'sender's Email'
password=input("Enter your password: ")

reciever = 'Reciever's Email  '

message = """\
Subject: Hi There!
Form: {}
To: {}

This message was sent from python!
""".format(sender, reciever)

context = ssl.create_default_context()


# with port 587 check connection
'''
try:
    server = smtplib.SMTP(smtp_server, port)    
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender,password)
    print('It Worked!')
except Exception as e:
    print(e)
finally:
    server.quit()
'''

# for sending mail using port 465
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    #send mail here
    server.sendmail(sender,reciever,message)

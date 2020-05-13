import smtplib

conn = smtplib.SMTP('smtp-mail.outlook.com', 587) #email smpt server, port number

conn.ehlo() #connect to the server and start the connection
# 2** --> everything okay

conn.starttls() #encrypts the password when it is sent off

conn.login('rahul1601@hotmail.co.uk', '!pa55word!') #email, password to login
# When using gmail you must enable access of less secure apps to the email

conn.sendmail('rahul1601@hotmail.co.uk', 'rahul1601@icloud.com', 'Subject: Python\n\nSent from Python!!!!!')
#from, to, subject, main body
# If {} is returned everything went fine, a dictionary is created with all of the emails which failed to send

conn.quit()


import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl = True) #ssl is encryption and we do want to use it
conn.login('rahulj160102@gmail.com', '!Pa55word!')

conn.select_folder('INBOX', readonly=True) #set readonly to true unless you want to delete emails

UIDs = conn.search(['SINCE','20-Aug-2019']) #all of the emails since a specific date stored to unique IDs variable
print(UIDs) #prints list of unique ids from emails since 20 august 2019

rawMessage = conn.fetch([3602], ['BODY[]', 'FLAGS']) #stores information about the email

message = pyzmail.PyzMessage.factory(rawMessage[3602][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('bcc'))
# returns the indicated details of the email

print(message.text_part) #if this returns none then there was no text part
print(message.html_part) #shows if there was a html part or not

print(message.text_part.get_payload().decode('UTF-8')) #use utf-8 most of the time, but shown in charset method of text_part


print(conn.list_folders()) #view the folders for an email account
conn.select_folder('INBOX', readonly=False) #allows the inbox to be edited
conn.delete_messages([3602]) #delete email with specific unique id
#you can pass the whole unique ids list if you want to delete the whole list for emails after a certain date or something

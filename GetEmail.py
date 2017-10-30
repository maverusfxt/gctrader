# Python script to receive email via IMAP
# https://stackoverflow.com/questions/348392/receive-and-send-emails-in-python
	
# Found a helpful example for reading emails by connecting using IMAP:

# Python — imaplib IMAP example with Gmail

#import imaplib
#mail = imaplib.IMAP4_SSL('imap.gmail.com')
#mail.login('goldenechoalerts@gmail.com', 'm40K3NioJsB8')
#mail.list()
## Out: list of "folders" aka labels in gmail.
#mail.select("inbox") # connect to inbox.
#result, data = mail.search(None, "ALL")

#ids = data[0] # data is a list.
#id_list = ids.split() # ids is a space separated string
#latest_email_id = id_list[-1] # get the latest
#print ('ids=' + ids)
#print ('id_list=' + id_list)

# fetch the email body (RFC822) for the given ID
#result, data = mail.fetch(latest_email_id, "(RFC822)") 
#print ('result=' + result)
#print ('data=' + data)

#raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads
#print ("raw_email=" + raw_email)


# https://stackoverflow.com/questions/4908472/how-to-receive-mail-using-python
#import outlook
#mail = outlook.Outlook()
#mail.login('goldenechoalerts@outlook.com','m40K3NioJsB8')
#mail.inbox()
#print ('mail.unread=' + mail.unread())

##to retrive email element :

#print ('body=' + mail.mailbody())
#print ('subject=' + mail.mailsubject())
#print ('from=' + mail.mailfrom())
#print ('mailto=' + mail.mailto())

import poplib
from email import parser
pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('goldenechoalerts')
pop_conn.pass_('m40K3NioJsB8')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for part in message.walk():
    if part.get_content_type():
        body = part.get_payload(decode=True)
#for message in messages:
#    print (message['subject'])
#    print (message['body'])
pop_conn.quit()

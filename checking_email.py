import imapclient
import pyzmail
# imap address, ssl=True means we're using ssl encryption
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('stuartwilson94@gmail.com', 'hsqfwbrqsmthhazh')  # email, password
# readonly=True means we can't delete emails
conn.select_folder('INBOX', readonly=True)
# search for emails since 20 May 2023
UIDs = conn.search([b'SINCE', b'20-may-2023'])
# print(UIDs)  # print the unique ids of the emails
# fetch the raw message of the email with uid 76334
rawMessage = conn.fetch([76277], ['BODY[]', 'FLAGS'])
# print(rawMessage)
pyzmail.PyzMessage.factory(rawMessage[76277][b'BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessage[76277][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('bcc'))
print(message.text_part)  # returns None if there is no text part
print(message.html_part)  # returns None if there is no html part
print(message.text_part.get_payload().decode('UTF-8'))
conn.logout()

# imap search keys
# ALL
# BEFORE date
# ON date
# SINCE date
# SUBJECT string
# BODY string
# TEXT string
# FROM string
# TO string
# CC string
# BCC string
# SEEN
# UNSEEN
# ANSWERED
# UNANSWERED
# DELETED
# UNDELETED
# DRAFT
# UNDRAFT
# FLAGGED
# UNFLAGGED
# LARGER n
# SMALLER n
# NOT search-key
# OR search-key1 search-key2
# search-key1 search-key2
# UID sequence-set
# UID sequence-set
# X-GM-RAW string

conn.list_folders()  # list all folders

# conn.select_folder('INBOX', readonly=False)  # select inbox folder
# UIDs = conn.search(['ON', '24-May-2023'])  # search for emails on 24 May 2023
# conn.delete_messages(UIDs)  # delete the emails

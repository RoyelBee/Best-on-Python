import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = ['rejaul.islam@transcombd.com', '']
cc = ['', '']
bcc = ['', '']

recipient = to + cc + bcc

subject = "Test report "

email_server_host = 'mail.transcombd.com'
port = 25

msgRoot['From'] = me

msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msg = MIMEMultipart()
msgRoot.attach(msg)
#
# msgText = MIMEText('This is the alternative plain text message.')
# msgAlternative.attach(msgText)

msgText = MIMEText(""" 
                     <img src="cid:img">
                    
                    """, 'html')

msg.attach(msgText)

# --------- Set Credit image in mail   -----------------------
img = open('D:/Python Code/Best-on-Python/box.png', 'rb')
img = MIMEImage(img.read())
# img.close()
#
img.add_header('Content-ID', '<img>')
msgRoot.attach(img)

# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()
print('Mail Send')

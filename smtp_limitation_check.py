# import smtplib
# smtp = smtplib.SMTP('mail.transcombd.com', 25)
# smtp.ehlo()
# max_limit_in_bytes = int( smtp.esmtp_features['size'] )
#
# print(max_limit_in_bytes)

import smtplib
smtp_server = 'smtp.gmail.com'
port = 2525
login = 'rejaultranscombd@gmail.com'
password = 'erp.rejauL'

sender = 'rejaultranscombd@gmail.com'
receiver = 'royelsoft@gmail.com'
message = f"""\
Subject: Hi there
To: {receiver}
From: {sender}
This is my first message with Python."""

with smtplib.SMTP(smtp_server, port) as server:
  server.login(login, password)
  server.sendmail(sender, receiver, message)
print('Sent')

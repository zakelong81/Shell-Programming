import smtplib, os
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
with open("new.cvs") as new:
    headn = [next(new) for x in xrange(5)]
with open("old.cvs") as old:
    heado = [next(new) for x in xrange(5)]
print(headn)
print(heado)
if headn != heado:
    msg = MIMEMultipart()
    msg['From'] = 'zakelong81@gmail.com'
    msg['To'] = 'zakelong81@gmail.com'
    msg['Subject'] = 'Top 5 has changed'
    message = 'SAM ??????'
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('gmail-smtp-in.l.google.com')
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('zakelong81@gmail.com')
    mailserver.sendmail('zakelong81@gmail.com','zakelong81@gmail.com',msg)
    mailserver.quit()
    print("sent mail")
else :
    print("nothing sent")
os.rename('new.cvs', 'old.cvs')

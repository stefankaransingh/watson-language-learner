import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from local import SENDER_EMAIL,SENDER_EMAIL_PASSWORD

def send_email(email,subject,text):
	html ="""
		<html>
		  <head></head>
		  <body>
			{0}
		  </body>
		</html>
	"""
	email_body =html.format(text)
	# Gmail Sign In
	gmail_sender =  SENDER_EMAIL
	gmail_passwd =  SENDER_EMAIL_PASSWORD

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_sender, gmail_passwd)

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = gmail_sender
	msg['To'] = email
	msg.attach(MIMEText(email_body, 'html'))
	try:
		server.sendmail(gmail_sender, [email], msg.as_string())
		print ('email sent')
	except:
		print ('error sending mail')

	server.quit()

import smtplib
EMAIL_ADDRESS = os.environ["ADMIN_EMAIL"]
PASSWORD = os.environ["ADMIN_PASSWORD"]

def send_email(subject, msg, email):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(EMAIL_ADDRESS, PASSWORD)
		message = 'Subject:{}\n\n{}'.format(subject,msg)
		server.sendmail(EMAIL_ADDRESS, email, message)
		server.quit()
		print("Success")
	except:
		print("Email failed to send.")
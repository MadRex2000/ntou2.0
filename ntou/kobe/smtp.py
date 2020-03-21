from email.mime.text import MIMEText
import smtplib, configparser

class sendMail():
	def __init__(self, to):
		self.to = to
		self.config = configparser.ConfigParser()
		self.config.read('smtpconfig.ini')
		self.user = self.config.get('SMTP', 'user')
		self.pswd = self.config.get('SMTP', 'pswd')
		content = '您好，您在靠北海大2.0的審核者註冊已經通過。'
		self.mime = MIMEText(content, 'html', 'utf-8')
		self.mime['To'] = self.to
		self.mime['Subject'] = '歡迎成為 KobeNTOU2.0 審核者'
		self.mime['From'] = self.user

	def send(self):
		try:
			obj = smtplib.SMTP('mail.gandi.net', 587)
			obj.ehlo()
			obj.starttls()
			obj.login(self.user, self.pswd)
			obj.sendmail(self.user, self.to, self.mime.as_string())
			obj.close()
			return True
		except:
			return False
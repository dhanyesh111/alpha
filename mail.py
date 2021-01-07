import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from concurrent.futures.thread import ThreadPoolExecutor
import time

print("d0")
msg = MIMEMultipart()
msg["from"] = "qq003501@gmail.com"
msg["to"] = "tkirankanakan@gmail.com"
msg["Subject"] = "say my name"
print("d1")
html_body = MIMEText("<h1>say my name<h1>", "html")
data = MIMEBase("application", "octet-stream")
f = open("demofile.txt", "rb")
payload = f.read()
f.close()
data.set_payload(payload)
encoders.encode_base64(data)
data.add_header("Content-Disposition", "attachment", filename="hellow")
msg.attach(data)
message = msg.as_string()
t=ThreadPoolExecutor()
def send():
    smtp = smtplib.SMTP("smtp.gmail.com", "587")
    smtp.ehlo()
    smtp.starttls()
    smtp.login("qq003501@gmail.com", "POLKMN@123")
    smtp.sendmail(msg["from"], msg["to"], message)
for i in range (1):
    t.submit(send)
    print(i)"""
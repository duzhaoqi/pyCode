import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time



username="linuxbug@163.com"
password="*******"
login=(username,password)
receive = "1147705876@qq.com"
subject = "Hello,Mr.du"

info = ("<h2>nihao</h2>",)


def email_163_simple(login,receive,subject,args):
    smtp = smtplib.SMTP("smtp.163.com")
    smtp.login(login[0],login[1])
    sender = login[0]
    receive = receive
    try:
        text = MIMEText(args[0],_subtype="html")
        message=MIMEMultipart()
        message.attach(text)

        message["from"]=sender
        message["to"]=receive
        message["subject"]=subject

        smtp.sendmail(sender,receive,message.as_string())
    except Exception as e:
        print(e)
    finally:
        smtp.quit()


if __name__ == "__main__":
    email_163_simple(login,receive,subject,info)

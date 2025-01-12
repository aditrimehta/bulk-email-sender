from email.message import EmailMessage
from senderinfo import email, password
from email.utils import formataddr
import smtplib

#senderinfo is a python file that contains sender gmail and "App password" stored in email and password variables 

#this is the port and server for gmail. outlook has different one
#this code uses tls
PORT=587
EMAIL_SERVER="smtp.gmail.com"


#customise ur parameters and edit code (change the same in main file too) 
def send_email(subject,reciever_email,name,duedate,appnumber,amount):
    msg=EmailMessage()
    msg["Subject"]=subject
    msg["From"]=formataddr(("From Aditri:)",f"{email}"))
    msg["To"]=reciever_email
    # customise content
    msg.set_content(
        f"""\
        Hi {name}, friend no: {appnumber},
        This is a test email.
        I hope I annoy u with this.
        This is ur due date to give me a gift: {duedate}.
        It should be worth Rs{amount}.
        From,
        Aditri:)
        """
    )
    #add html content for better formating
    msg.add_alternative(
        f"""\
<html>
    <body>
        <p>Hi <strong>{name}</strong>, friend no: <strong>{appnumber}</strong>,</p>
        <p>This is a test email.</p>
        <p>I hope I annoy u with this.</p>
        <p>This is ur due date to give me a gift: <strong>{duedate}</strong>.</p>
        <p>It should be worth <strong>Rs{amount}</strong>.</p>
        <p>From,</p>
        <p>Aditri:)</p>
    </body>
</html>
        """,
        subtype="html",
    )
    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
        server.starttls()
        server.login(email,password)
        server.sendmail(email,reciever_email,msg.as_string())

if __name__=="__main__":
    send_email(
        subject="Annoyance",
        name="aditri",
        reciever_email="aditriamitmehta@gmail.com",
        duedate="12-01-25",
        appnumber="1",
        amount="1 million",
    )
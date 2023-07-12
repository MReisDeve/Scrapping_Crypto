import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
from datetime import datetime


class Mail_Sender:

    def __init__(self,mail_server, port, sender, receiver, subject, body_msg='', attachment_file_path=None):
        self.mail_server = mail_server
        self.port = port
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body_msg = body_msg
        self.attachment_file_path = attachment_file_path
        self.password = getpass(prompt="Informe a senha da sua conta de email:")
        self.email_msg = self.setup_email_msg()
        self.attach_file_to_email()


    def setup_email_msg(self):
        email_msg = MIMEMultipart()
        email_msg["From"] = self.sender
        email_msg["To"] = self.receiver
        email_msg["Subject"] = self.subject
        email_msg.attach(MIMEText(self.body_msg, "plain"))
        return email_msg

    def attach_file_to_email(self):
        file_path = self.attachment_file_path
        if file_path:
            with open(file_path, "r") as f_attach:
                part = MIMEBase(_maintype="text", _subtype="csv")
                part.set_payload(f_attach.read())
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename=crypto_data_{str(datetime.now()).split(' ')[0]}.csv",
                )

            self.email_msg.attach(part)
    
    def send_mail(self):
        ssl_context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.mail_server, self.port, context=ssl_context) as server:
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, self.email_msg.as_string())
import win32com.client
from email.message import EmailMessage

from models.users import Receiver, Sender

class EmailClient():
    def __init__(self, sender: Sender, subject: str):
        self.sender = sender
        self.subject = subject
        outlook = win32com.client.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.Subject = subject
        self.mail = mail

        
    def setup_receiver(self, receiver, body):
        self.mail.To = receiver.email
        self.mail.HTMLBody = body
        
    def send_email(self):
        try:
            self.mail.Send()
            print("Email sent!")
        except Exception:
            print("Did not send email")
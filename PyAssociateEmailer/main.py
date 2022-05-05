from email_setup.base_email import BaseEmail
from email_setup.send_email import EmailClient
from models.technology import TechStack
from models.users import Receiver, Sender
from user_input.setup_config import Contacts, TechStackCfg


def main():

    print("Beginning auto email send")

    trainer = Contacts.get_trainer()
    associates = Contacts.get_associates()
    tech_stack = TechStackCfg.get_tech_stack()
    tech = TechStack(tech_stack["name"], tech_stack["length"], tech_stack["repo"], tech_stack["class"], tech_stack["zoom"], tech_stack["slack"], tech_stack["survey"], tech_stack["start"])

    sender = Sender(trainer[0], trainer[1])

    subject = "Welcome to Revature and Training!"
    
    for associate in associates:
        email_client = EmailClient(sender, subject)
        receiver = Receiver(associate[0], associate[1])
        emailMaker = BaseEmail(sender, receiver, tech)
        message = emailMaker.setup_email_body()
        email_client.setup_receiver(receiver, message)
        try:
            email_client.send_email()
            print(f"Successfully sent to {receiver.name} : {receiver.email}")
        except Exception:
            print(f"Failed to send email to {receiver.name} : {receiver.email}")

if __name__ == '__main__':
    main()
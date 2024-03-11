"""
[Dependency Inversion Principle (DIP)] Download the python file from this link. 
Suppose we have a NotificationService class that is responsible for sending notifications. 
The NotificationService class directly depends on the EmailSender class to send emails.
"""


from abc import ABC,abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send_email(self,recipient,subject,message):
        pass

class EmailSender(MessageSender):
    def send_email(self, recipient, subject, message):
        # Code to send an email
        print(f"Sending email to {recipient}: {subject} - {message}")

class NotificationService:
    def __init__(self,source:MessageSender):
        self.email_sender = source

    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)

# Using the NotificationService to send a notification
notification_service = NotificationService(EmailSender())
notification_service.send_notification("user@example.com", "Hello, this is a notification!")



"""
class EmailSender:
    def send_email(self, recipient, subject, message):
        # Code to send an email
        print(f"Sending email to {recipient}: {subject} - {message}")

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)

# Using the NotificationService to send a notification
notification_service = NotificationService()
notification_service.send_notification("user@example.com", "Hello, this is a notification!")
"""
"""
email.py
This file contains the Email class with a method for sending emails.
"""

class Email:
    def send_email(self, recipient: str, subject: str, message: str) -> str:
        """
        Sends an email to the specified recipient.
        Args:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The content of the email.
        Returns:
            str: The status message indicating whether the email was sent successfully or not.
        """
        # Implementation goes here

"""
participant.py
This file contains the Participant class and its methods.
"""

class Participant:
    def __init__(self, name: str, email: str):
        """
        Initializes a Participant object.
        Args:
            name (str): The name of the participant.
            email (str): The email address of the participant.
        """
        self.name = name
        self.email = email

    def add_participant(self, survey: Survey) -> str:
        """
        Adds the participant to the specified survey.
        Args:
            survey (Survey): The survey to add the participant to.
        Returns:
            str: The status message indicating whether the participant was added successfully or not.
        """
        # Implementation goes here

    def remove_participant(self, survey: Survey) -> str:
        """
        Removes the participant from the specified survey.
        Args:
            survey (Survey): The survey to remove the participant from.
        Returns:
            str: The status message indicating whether the participant was removed successfully or not.
        """
        # Implementation goes here

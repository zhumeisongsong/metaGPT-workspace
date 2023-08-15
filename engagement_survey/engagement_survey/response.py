## response.py

class Response:
    def __init__(self, participant, answers):
        """
        Initializes a Response object.
        Args:
            participant (Participant): The participant who submitted the response.
            answers (List[Answer]): The list of answers provided by the participant.
        """
        self.participant = participant
        self.answers = answers

class Answer:
    def __init__(self, question, value):
        """
        Initializes an Answer object.
        Args:
            question (Question): The question being answered.
            value (str): The value of the answer.
        """
        self.question = question
        self.value = value

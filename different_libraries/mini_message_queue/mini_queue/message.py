
from uuid import uuid4


class Message:
    def __init__(self, text: str) -> None:
        self.text = text

    @property
    def id(self):
        return uuid4()

    def __repr__(self) -> str:
        return "Message(id=" + str(self.id) + ", payload=" + '"' +str(self.text) + '"' + ")"

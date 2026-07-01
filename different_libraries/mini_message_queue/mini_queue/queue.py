from collections import deque

class Queue:
    def __init__(self):
        self._messages = deque()

    def consume(self):
        return self._messages.popleft()

    def is_empty(self):
        return bool(self._messages)

    def publish(self, message):
        self._messages.append(message)

    def __len__(self):
        return len(self._messages)

    def __repr__(self):
        return f"<Queue at {hex(id(self))}>"

    def __str__(self):
        return f"<Queue at {hex(id(self))}, size={len(self)}>"

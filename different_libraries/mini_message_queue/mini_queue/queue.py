from collections import deque

class Queue:
    def __init__(self):
        self._messages = deque()

    def publish(self, message):
        self._messages.append(message)

    def consume(self):
        return self._messages.popleft()

    def __len__(self):
        return len(self._messages)

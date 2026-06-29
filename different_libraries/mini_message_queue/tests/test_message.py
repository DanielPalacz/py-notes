from mini_queue.message import Message

def test_message_repr():
    msg = Message("text1")

    assert str(msg).startswith("Message(")
    assert str(msg).split(", ")[1] == 'payload="text1")'
    # Message(id=4acee5d0-5f06-4711-8430-7abb86fb5761, payload="text1")
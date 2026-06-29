from mini_queue.message import Message
from mini_queue.queue import Queue
from mini_queue.broker import Broker

Q = Queue()
print(len(Q), "- Num of Q elements after Queue creation")
broker = Broker(Q)
print(len(Q), "- Num of Q elements after linking with Broker")

msg = Message("text1")
broker.publish(msg)
print(len(Q), "- Num of Q elements after 1st publishing message by Broker")

msg_2 = Message("text2")
broker.publish(msg_2)
print(len(Q), "- Num of Q elements after 2nd publishing message by Broker")

msg_from_queue = broker.consume()

print(len(Q), "- Num of Q elements after consuming one message by Broker")

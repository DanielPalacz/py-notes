from mini_queue.message import Message
from mini_queue.queue import Queue
from mini_queue.broker import Broker

Q = Queue("def")

print(len(Q), "- Num of Q elements after Queue creation. Q =", Q)
broker = Broker()
broker.add_queue(Q)
print(broker)

msg = Message("text1")
broker.publish(msg, Q.name)
print(len(Q), "- Num of Q elements after 1st publishing message by Broker. Q =", Q)

msg_2 = Message("text2")
broker.publish(msg_2, Q.name)
print(len(Q), "- Num of Q elements after 2nd publishing message by Broker. Q =", Q)


# try:
#     msg_from_queue = broker.consume()
#     print(len(Q), "- Num of Q elements after consuming one message by Broker. Q =", Q)
#     print(msg_from_queue)
#
#     msg_from_queue = broker.consume()
#     print(msg_from_queue)
#     msg_from_queue = broker.consume()
# except IndexError as e:
#     print(f"Queue was empty ({e}, {Q}).")



msg_3 = Message("text3")
broker.publish(msg_3, Q.name)

Q1 = Queue("1st queue")
broker.add_queue(Q1)
broker.publish(msg_3, Q1.name)


Q2 = Queue("2nd queue")
broker.add_queue(Q2)

print(broker)


print()
for key_q, q in broker._queues.items():
    print(key_q, q, len(q))


#

msg_from_queue = broker.consume(Q.name)
print()
for key_q, q in broker._queues.items():
    print(key_q, q, len(q))

try:
    msg_from_queue = broker.consume(Q2.name)
except IndexError as e:
    print()
    print(f"Queue was empty ({e}, {Q2.name}, {Q2}).")

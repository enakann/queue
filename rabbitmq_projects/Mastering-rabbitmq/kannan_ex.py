#!/usr/bin/python
import pika
import inspect
import sys

msg=str(sys.argv[1])

print("connecting to rabbitmq broker")
credentials = pika.PlainCredentials('kannan','divya123')
connection=pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-2','5672','/',credentials))

channel=connection.channel()


channel.basic_publish(exchange='kannan',routing_key='test.kannan',mandatory=True,body=msg)

#print(inspect.getsource(channel.basic_publish))
#print(inspect.getsourcefile(channel.basic_publish))
#print(arg)

print("done sending")
connection.close()

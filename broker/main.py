import time
import unittest


# Broker
class Broker:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, subscriber):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(subscriber)

    def publish(self, topic, message):
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                subscriber.receive_message(topic, message)


# Subscriber
class Subscriber:
    def __init__(self, name):
        self.name = name
        self.received_messages = []

    def receive_message(self, topic, message):
        self.received_messages.append((topic, message))


# Unit Tests
class BrokerTest(unittest.TestCase):
    def test_broker_publish_single_subscriber(self):
        broker = Broker()
        subscriber = Subscriber("Alice")
        broker.subscribe("news", subscriber)

        message = "Breaking news: New discovery!"
        broker.publish("news", message)

        self.assertEqual(len(subscriber.received_messages), 1)
        self.assertEqual(subscriber.received_messages[0][0], "news")
        self.assertEqual(subscriber.received_messages[0][1], message)

    def test_broker_publish_multiple_subscribers(self):
        broker = Broker()
        subscriber1 = Subscriber("Alice")
        subscriber2 = Subscriber("Bob")
        broker.subscribe("news", subscriber1)
        broker.subscribe("news", subscriber2)

        message = "Breaking news: New discovery!"
        broker.publish("news", message)

        self.assertEqual(len(subscriber1.received_messages), 1)
        self.assertEqual(subscriber1.received_messages[0][0], "news")
        self.assertEqual(subscriber1.received_messages[0][1], message)

        self.assertEqual(len(subscriber2.received_messages), 1)
        self.assertEqual(subscriber2.received_messages[0][0], "news")
        self.assertEqual(subscriber2.received_messages[0][1], message)


if __name__ == '__main__':
    unittest.main()

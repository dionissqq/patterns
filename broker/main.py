import time


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
            print(f"Broker: Publishing message '{message}' on topic '{topic}'")
            for subscriber in self.subscribers[topic]:
                subscriber.receive_message(topic, message)
            print("")


# Subscriber
class Subscriber:
    def __init__(self, name):
        self.name = name

    def receive_message(self, topic, message):
        print(f"{self.name}: Received message '{message}' on topic '{topic}'")


# Usage
if __name__ == '__main__':
    broker = Broker()

    # Create subscribers
    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")
    subscriber3 = Subscriber("Charlie")

    # Subscribe subscribers to topics
    broker.subscribe("news", subscriber1)
    broker.subscribe("news", subscriber2)
    broker.subscribe("sports", subscriber2)
    broker.subscribe("weather", subscriber3)

    # Publish messages to topics
    broker.publish("news", "Breaking news: New discovery!")
    time.sleep(1)
    broker.publish("sports", "Goal! The home team takes the lead.")
    time.sleep(1)
    broker.publish("weather", "Sunny skies expected tomorrow.")

    # Unsubscribe a subscriber
    broker.subscribers["news"].remove(subscriber2)

    # Publish message after unsubscribe
    time.sleep(1)
    broker.publish("news", "Important announcement!")

    # Subscribe a new subscriber
    subscriber4 = Subscriber("Eve")
    broker.subscribe("news", subscriber4)

    # Publish message after new subscription
    time.sleep(1)
    broker.publish("news", "Latest update: Event rescheduled")

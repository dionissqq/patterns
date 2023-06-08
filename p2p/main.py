import time


class Peer:
    def __init__(self, name):
        self.name = name
        self.message_queue = []

    def send_message(self, recipient, message):
        self.message_queue.append((recipient, message))

    def process_messages(self):
        while self.message_queue:
            recipient, message = self.message_queue.pop(0)
            print(f"{self.name} sends message to {recipient.name}: {message}")
            time.sleep(0.5)  # Simulate network latency
            recipient.receive_message(self, message)

    def receive_message(self, sender, message):
        print(f"{self.name} receives message from {sender.name}: {message}")


# Usage
if __name__ == '__main__':
    # Create peers
    alice = Peer("Alice")
    bob = Peer("Bob")
    charlie = Peer("Charlie")

    # Exchange messages
    alice.send_message(bob, "Hello Bob!")
    bob.send_message(charlie, "Hi Charlie!")
    charlie.send_message(alice, "Hey Alice!")

    # Process messages
    alice.process_messages()
    bob.process_messages()
    charlie.process_messages()

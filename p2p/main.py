import time
import unittest


class Peer:
    def __init__(self, name):
        self.name = name
        self.received_messages = []

    def send_message(self, recipient, message):
        recipient.receive_message(self.name, message)

    def receive_message(self, sender, message):
        self.received_messages.append((sender, message))


class PeerToPeerTest(unittest.TestCase):
    def test_peer_to_peer_communication(self):
        alice = Peer("Alice")
        bob = Peer("Bob")
        charlie = Peer("Charlie")

        alice.send_message(bob, "Hello Bob!")
        bob.send_message(charlie, "Hi Charlie!")
        charlie.send_message(alice, "Hey Alice!")

        time.sleep(1)  # Wait for message propagation

        # Assert messages received by peers
        self.assertEqual(len(alice.received_messages), 1)
        self.assertEqual(alice.received_messages[0][0], "Charlie")
        self.assertEqual(alice.received_messages[0][1], "Hey Alice!")

        self.assertEqual(len(bob.received_messages), 1)
        self.assertEqual(bob.received_messages[0][0], "Alice")
        self.assertEqual(bob.received_messages[0][1], "Hello Bob!")

        self.assertEqual(len(charlie.received_messages), 1)
        self.assertEqual(charlie.received_messages[0][0], "Bob")
        self.assertEqual(charlie.received_messages[0][1], "Hi Charlie!")


if __name__ == '__main__':
    unittest.main()

import unittest


class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def unsubscribe(self, event_type, callback):
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(callback)

    def publish(self, event_type, data=None):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)


class EventBusTest(unittest.TestCase):
    def test_event_bus(self):
        bus = EventBus()

        events = []

        def event_callback_1(data):
            events.append(f"Callback 1: {data}")

        def event_callback_2(data):
            events.append(f"Callback 2: {data}")

        bus.subscribe("event_type", event_callback_1)
        bus.subscribe("event_type", event_callback_2)

        bus.publish("event_type", "Hello, World!")

        self.assertEqual(len(events), 2)
        self.assertIn("Callback 1: Hello, World!", events)
        self.assertIn("Callback 2: Hello, World!", events)

        bus.unsubscribe("event_type", event_callback_2)

        bus.publish("event_type", "This event won't trigger the second callback.")

        self.assertEqual(len(events), 3)
        self.assertIn("Callback 1: This event won't trigger the second callback.", events)
        self.assertNotIn("Callback 2:", events)


if __name__ == '__main__':
    unittest.main()

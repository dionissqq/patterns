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


# Usage
if __name__ == '__main__':
    def event_callback(data):
        print("Event occurred:", data)

    bus = EventBus()
    bus.subscribe("event_type", event_callback)

    bus.publish("event_type", "Hello, World!")

    bus.unsubscribe("event_type", event_callback)

    bus.publish("event_type", "This event won't trigger the callback.")

import random


class Model:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def remove_data(self, item):
        if item in self.data:
            self.data.remove(item)

    def get_data(self):
        return self.data


class View:
    def render(self, data):
        print("View - Displaying data:")
        for item in data:
            print("- " + str(item))


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item(self, item):
        self.model.add_data(item)
        self.update_view()

    def remove_item(self, item):
        self.model.remove_data(item)
        self.update_view()

    def update_view(self):
        data = self.model.get_data()
        self.view.render(data)


# Usage
if __name__ == '__main__':
    # Create instances of Model, View, and Controller
    model = Model()
    view = View()
    controller = Controller(model, view)

    # Add random items to the model
    items = ["Apple", "Banana", "Orange", "Grape", "Mango"]
    for _ in range(5):
        random_item = random.choice(items)
        controller.add_item(random_item)

    # Remove an item from the model
    item_to_remove = random.choice(model.get_data())
    controller.remove_item(item_to_remove)

import unittest
from unittest.mock import patch
from io import StringIO


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


class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model, self.view)

    def test_add_item(self):
        self.controller.add_item("Apple")
        self.assertEqual(self.model.get_data(), ["Apple"])

    def test_remove_item(self):
        self.model.add_data("Apple")
        self.model.add_data("Banana")
        self.controller.remove_item("Apple")
        self.assertEqual(self.model.get_data(), ["Banana"])

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_view(self, mock_stdout):
        self.model.add_data("Apple")
        self.model.add_data("Banana")
        self.controller.update_view()
        expected_output = "- Apple\n- Banana\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()

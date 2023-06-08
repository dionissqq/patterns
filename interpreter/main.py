import unittest


class Context:
    def __init__(self):
        self.input = ""
        self.output = ""

    def get_input(self):
        return self.input

    def set_input(self, input_text):
        self.input = input_text

    def get_output(self):
        return self.output

    def set_output(self, output_text):
        self.output = output_text


class Expression:
    def interpret(self, context):
        pass


class ReverseExpression(Expression):
    def interpret(self, context):
        input_text = context.get_input()
        reversed_text = input_text[::-1]
        context.set_output(reversed_text)


class CapitalizeExpression(Expression):
    def interpret(self, context):
        input_text = context.get_input()
        capitalized_text = input_text.upper()
        context.set_output(capitalized_text)


class InterpreterTest(unittest.TestCase):
    def test_reverse_expression(self):
        context = Context()
        input_text = "Hello, World!"
        expected_output = "!dlroW ,olleH"

        context.set_input(input_text)
        reverse_expression = ReverseExpression()
        reverse_expression.interpret(context)
        actual_output = context.get_output()

        self.assertEqual(actual_output, expected_output)

    def test_capitalize_expression(self):
        context = Context()
        input_text = "Hello, World!"
        expected_output = "HELLO, WORLD!"

        context.set_input(input_text)
        capitalize_expression = CapitalizeExpression()
        capitalize_expression.interpret(context)
        actual_output = context.get_output()

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

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


# Usage
if __name__ == '__main__':
    context = Context()

    # Set the input text
    context.set_input("Hello, World!")

    # Use the ReverseExpression to reverse the input
    reverse_expression = ReverseExpression()
    reverse_expression.interpret(context)
    reverse_output = context.get_output()
    print(reverse_output)  # Output: "!dlroW ,olleH"

    # Use the CapitalizeExpression to capitalize the input
    capitalize_expression = CapitalizeExpression()
    capitalize_expression.interpret(context)
    capitalize_output = context.get_output()
    print(capitalize_output)  # Output: "!DLROW ,OLLEH"

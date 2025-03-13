import logging
from app.commands import Command

class DivideCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        """Perform the division of two numbers, raising an error if the denominator is zero."""
        if b == 0:
            raise ZeroDivisionError('Cannot divide by 0!')
        return a / b

    def execute(self, *args, **kwargs):
        """Execute the division command."""
        a, b = map(float, args)  # Convert inputs to float
        result = self.evaluate(a, b)  # Get the result of the division
        logging.info(f'{a} / {b} = {result}')  # Log the operation
        print(f'{a} / {b} = {result}')  # Print the result
        return result  # Return the result for command history
    
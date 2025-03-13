import logging
from app.commands import Command

class MultiplyCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        """Perform the multiplication of two numbers."""
        return a * b

    def execute(self, *args, **kwargs):
        """Execute the multiplication command."""
        a, b = map(float, args)  # Convert inputs to float
        result = self.evaluate(a, b)  # Get the result of the multiplication
        logging.info(f'{a} x {b} = {result}')  # Log the operation
        print(f'{a} x {b} = {result}')  # Print the result
        return result  # Return the result for command history
            
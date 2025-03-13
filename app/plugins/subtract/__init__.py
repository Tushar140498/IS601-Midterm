import logging
from app.commands import Command

class SubtractCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        """Perform the subtraction of two numbers."""
        return a - b

    def execute(self, *args, **kwargs):
        """Execute the subtraction command."""
        a, b = map(float, args)  # Convert inputs to float
        result = self.evaluate(a, b)  # Get the result of the subtraction
        logging.info(f'{a} - {b} = {result}')  # Log the operation
        print(f'{a} - {b} = {result}')  # Print the result
        return result  # Return the result for command history
            
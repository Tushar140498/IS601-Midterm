from app.commands import Command
import logging

class AddCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        """Perform the addition of two numbers."""
        return a + b

    def execute(self, *args, **kwargs):
        """Execute the addition command."""
        # Ensure args are converted to floats
        a, b = map(float, args)
        result = self.evaluate(a, b)  # Get the result of the addition
        logging.info(f'{a} + {b} = {result}')  # Log the operation
        print(f'{a} + {b} = {result}')  # Print the result
        return result  # Return the result for command history
        
from app.commands import Command
import logging

class AddCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a + b

    def execute(self, *args, **kwargs):
        # Ensure args are converted to floats
        a, b = map(float, args)
        logging.info(f'{a} + {b} = {self.evaluate(a, b)}')
        print(f'{a} + {b} = {self.evaluate(a, b)}')
        
    
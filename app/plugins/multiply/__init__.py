import logging
from app.commands import Command

class MultiplyCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a * b

    def execute(self, *args, **kwargs):
        a, b = map(float, args)  # Convert inputs to float
        logging.info(f'{a} x {b} = {self.evaluate(a, b)}')
        print(f'{a} x {b} = {self.evaluate(a, b)}')
        
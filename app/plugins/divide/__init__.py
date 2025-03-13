import logging
from app.commands import Command

class DivideCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError('Cannot divide by 0!')
        return a / b

    def execute(self, *args, **kwargs):
        a, b = map(float, args)  # Convert inputs to float
        logging.info(f'{a} / {b} = {self.evaluate(a, b)}')
        print(f'{a} / {b} = {self.evaluate(a, b)}')
        
from app.commands import Command

class SubtractCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a - b

    def execute(self, *args, **kwargs):
        a, b = map(float, args)  # Convert inputs to float
        print(f'{a} - {b} = {self.evaluate(a, b)}')
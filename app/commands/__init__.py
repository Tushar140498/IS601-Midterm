from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        """Abstract method to execute the command with given arguments."""
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}  # Dictionary to store command names and their corresponding command classes
        self.history = []   # List to store command history

    def register_command(self, command_name: str, command: Command):
        """Registers a command with its corresponding name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        """ 
        Execute the command by its name, passing any arguments.
        
        Args:
            command_name (str): The name of the command (e.g., 'add', 'subtract').
            *args: The extra arguments for the command (e.g., numbers a and b).
        """
        try:
            # Exclude 'history' and 'menu' commands from being recorded
            if command_name in ['history', 'menu']:
                self.commands[command_name].execute(*args)
                return
            
            # Execute the command and store the result
            result = self.commands[command_name].execute(*args)
            # Append command, arguments, and result in the desired format
            self.history.append(f"{command_name} {' '.join(args)} = {result}")  # Append formatted command and result
            
        except KeyError:
            print(f"No such command: {command_name}")
        except ValueError:
            print("Enter valid numbers for the operation.")
        except Exception as e:
            print(f"Error executing command '{command_name}': {e}")

from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for all commands."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Abstract method that must be implemented by all command classes.
        It should define the specific behavior when the command is executed.
        """
        pass
    
class CommandHandler:
    def __init__(self):
        self.commands = {}  # Dictionary to store command names and their corresponding command classes
    
    def register_command(self, command_name: str, command: Command):
        """Registers a command with its corresponding name."""
        self.commands[command_name] = command
    
    def execute_command(self, command_name: str, *args):
        """ 
        Execute the command by its name, passing any arguments (e.g., numbers a and b).
        command_name: The name of the command (e.g., 'add', 'subtract')
        *args: The extra arguments for the command (e.g., numbers a and b)
        """
        try:
            if command_name not in self.commands:
                raise KeyError(f"{command_name} command is not available.")
            
            # Execute the command
            self.commands[command_name].execute(*args)
        
        except KeyError:
            print(f"No such command: {command_name}")
        except ValueError:
            print("Enter valid numbers for the operation.")
        except Exception as e:
            print(f"Error executing command '{command_name}': {e}")
            
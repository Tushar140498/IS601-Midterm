import os
import sys
import pkgutil
import importlib

from app.commands import Command, CommandHandler  # Importing command base classes

class App:
    def __init__(self):
        self.command_handler = CommandHandler()  # Initialize the CommandHandler to manage commands
    
    def load_plugins(self):
        # Dynamically load all plugins from the 'app.plugins' directory
        plugins_package = 'app.plugins'
        # Iterate through the plugins folder to find and load all command plugins
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', os.sep)]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        # Register the command if it's a subclass of Command
                        if issubclass(item, Command):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue
    
    def start(self):
        # Load all available plugins (commands)
        self.load_plugins()

        print(f"Available commands: {', '.join(list(self.command_handler.commands.keys()))}")
        print(f"Usage: Command num1 num2 (Ex: add 3 4) or type 'exit' to exit.\n")

        while True:  # REPL (Read, Evaluate, Print, Loop)
            user_input = input(">>> ").strip().split(" ")
            command_name = user_input[0]
            
            if command_name == 'exit':
                # print("Exiting...")
                sys.exit("Exiting...")  # Explicitly raise SystemExit for test to catch
            
            # Run the specified command with provided arguments
            self.command_handler.execute_command(command_name, *user_input[1:])
            
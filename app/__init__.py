import os
import sys
import pkgutil
import importlib
from dotenv import load_dotenv # type: ignore
import logging
import logging.config

from app.commands import Command, CommandHandler

class App:
    def __init__(self):
        self.command_handler = CommandHandler()  # Initialize the CommandHandler to manage commands
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'DEVELOPMENT')

    def configure_logging(self):
        """Configure logging settings."""
        log_directory = 'logs'
        log_file_path = os.path.join(log_directory, 'app.log')

        # Create logs directory if it does not exist
        os.makedirs(log_directory, exist_ok=True)

        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, filename=log_file_path, 
                                format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Load environment variables from .env file."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        """Dynamically load all plugins from the 'app.plugins' directory."""
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """Register command classes from the plugin module."""
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        """Start the REPL for command input."""
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        print(f"Available commands: {', '.join(list(self.command_handler.commands.keys()))}")
        print(f"Usage: Command num1 num2 (Ex: add 3 4) or type 'exit' to exit.\n")

        while True:  # REPL (Read, Evaluate, Print, Loop)
            user_input = input(">>> ").strip().split(" ")
            command_name = user_input[0]
            
            if command_name == 'exit':
                logging.info("Application exit.")
                sys.exit(0)  # Use sys.exit(0) for a clean exit, indicating success.
            
            # Run the specified command with provided arguments
            try:
                self.command_handler.execute_command(command_name, *user_input[1:])
            except KeyError:
                logging.error(f"Unknown command: {command_name}")
                print(f"Unknown command: {command_name}")  # Output for user feedback
            except Exception as e:
                logging.error(f"Error executing command: {command_name}. Exception: {e}")
                print(f"Error executing command: {command_name}. Exception: {e}")  # Output for user feedback
from app.commands import Command

class MenuCommand(Command):
    def execute(self, *args, **kwargs):
        """Execute the menu command, displaying available commands."""
        self.display_menu()

    def display_menu(self):
        """Prints the available commands in the application."""
        print("Available Commands:")
        print("-------------------")
        print("add                : Add two numbers")
        print("subtract           : Subtract two numbers")
        print("multiply           : Multiply two numbers")
        print("divide             : Divide two numbers")
        print("history show       : Display command history")
        print("history delete <n> : Delete the n-th entry from history")
        print("history save       : Save command history to a file")
        print("history clear      : Clear the command history")
        print("exit               : Exit the application")
        print("-------------------")

# Register the MenuCommand when the application is initialized
menu_command = MenuCommand()
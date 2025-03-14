"""Test commands"""

from decimal import Decimal
import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.menu import MenuCommand
from app.plugins.exit import ExitCommand


@pytest.mark.parametrize(
    "a, b, command, expected", [
        (Decimal('10'), Decimal('5'), AddCommand, Decimal('15')),  # Test addition
        (Decimal('10'), Decimal('5'), SubtractCommand, Decimal('5')),  # Test subtraction
        (Decimal('10'), Decimal('5'), MultiplyCommand, Decimal('50')),  # Test multiplication
        (Decimal('10'), Decimal('2'), DivideCommand, Decimal('5')),  # Test division
        (Decimal('10.5'), Decimal('0.5'), AddCommand, Decimal('11.0')), #Test addition with decimal
        (Decimal('10.5'), Decimal('0.5'), SubtractCommand, Decimal('10.0')),  # Test subtraction
        (Decimal('10.5'), Decimal('2'), MultiplyCommand, Decimal('21.0')), # Test multiplication
        (Decimal('10'), Decimal('0.5'), DivideCommand, Decimal('20')), #Test division with decimals
    ]
)
# pylint: disable=invalid-name

def test_calculation_commands(
    a, b, command, expected
):
    """
    Test calculation commands with various scenarios.

    This test ensures that the command class correctly performs the arithmetic operation
    (specified by the 'command' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.

    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        command (function): The arithmetic command to perform.
        expected (Decimal): The expected result of the operation.
    """
    assert command().evaluate(
        a, b
    ) == expected, f"Failed {command.__name__} command with {a} and {b}"

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ZeroDivisionError
    """
    with pytest.raises(
        ZeroDivisionError, match="Cannot divide by 0!"
    ):  # Expect a ZeroDivisionError to be raised.
        DivideCommand().evaluate(
            Decimal(3), Decimal(0)
        )  # Attempt to perform the calculation, which should trigger the ZeroDivisionError.

def test_menu_display(capsys):
    """
    Test if the MenuCommand correctly displays available commands.
    
    This test captures the printed output of the `display_menu` function and 
    checks if it contains all expected commands.
    """
    menu = MenuCommand()
    menu.display_menu()

    captured = capsys.readouterr()
    output = captured.out

    # List of expected menu items
    expected_commands = [
        "add                : Add two numbers",
        "subtract           : Subtract two numbers",
        "multiply           : Multiply two numbers",
        "divide             : Divide two numbers",
        "history show       : Display command history",
        "history delete <n> : Delete the n-th entry from history",
        "history save       : Save command history to a file",
        "history clear      : Clear the command history",
        "exit               : Exit the application"
    ]

    for command in expected_commands:
        assert command in output, f"'{command}' not found in menu output"

def test_exit_command():
    """Test if ExitCommand properly exits the application."""
    exit_cmd = ExitCommand()
    
    with pytest.raises(SystemExit) as excinfo:
        exit_cmd.execute()

    assert str(excinfo.value) == "Exiting the program..."

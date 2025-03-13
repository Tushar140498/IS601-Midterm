"""Test commands"""

from decimal import Decimal
import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

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

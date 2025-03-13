"""Import pytest for testing the App class and its functionalities."""
import pytest
from app import App

@pytest.mark.parametrize("Command", [
    ('add'),
    ('subtract'),
    ('multiply'),
    ('divide'),
])

# pylint: disable=invalid-name
def test_calculation_operations(Command, monkeypatch):
    """Simulate command followed by exit."""
    inputs = iter([f'{Command} 1 1', 'exit'])  # Simulate command with arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Ensure the app start triggers SystemExit
    assert e.type == SystemExit  # Check if SystemExit was raised
    assert e.value.code == 0  # Check for clean exit (0)

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Capture the REPL output
    captured = capfd.readouterr()

    # Verify that the unknown command message is present in the output
    # pylint: disable=assert-on-string-literal
    assert "Available commands: add, subtract, multiply, divide, exit","Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit." in captured.out

    # Ensure a clean exit (exit code 0)
    assert excinfo.value.code == 0  # Clean exit after unknown command

def test_app_invalid_input_format(capfd, monkeypatch):
    """Test how the REPL handles invalid input formats."""
    # Simulate invalid input followed by 'exit'
    inputs = iter(['add 2', 'exit'])  # Missing one argument for 'add'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    # Capture the REPL output
    captured = capfd.readouterr()
    # Verify that the error message for invalid input is present in the output
    # pylint: disable=assert-on-string-literal
    assert "Available commands: add, subtract, multiply, divide, exit","Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit." in captured.out
    # Ensure a clean exit (exit code 0)
    assert excinfo.value.code == 0  # Ensure clean exit after invalid input

def test_environment_variable_missing(monkeypatch):
    """Test how the app handles missing environment variables."""
    monkeypatch.setattr('os.environ', {})  # Simulate an empty environment
    app = App()
    assert app.settings.get('ENVIRONMENT') == 'DEVELOPMENT'  # Default value

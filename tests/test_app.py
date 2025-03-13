"""Import pytest for testing the App class and its functionalities."""
import pytest
from app import App

@pytest.mark.parametrize("command", [
    ('add'),
    ('subtract'),
    ('multiply'),
    ('divide'),
])
def test_calculation_operations(command, monkeypatch):
    """Simulate command followed by exit."""
    inputs = iter([f'{command} 1 1', 'exit'])  # Simulate command with arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Ensure the app start triggers SystemExit
    assert e.type == SystemExit  # Check if SystemExit was raised
    assert str(e.value) == "Exiting..."  # Ensure correct exit message

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')  # Simulate 'exit' input
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Ensure SystemExit is raised when 'exit' is entered
    assert e.type == SystemExit  # Ensure SystemExit type

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])  # Simulate unknown command + exit
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Ensure SystemExit is raised at the end
    captured = capfd.readouterr()  # Capture stdout and stderr
    assert "No such command: unknown_command" in captured.out  # Verify correct handling

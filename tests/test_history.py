"""
Unit tests for the HistoryCommand class.
"""

import os
import pytest
import pandas as pd
from app.plugins.history import HistoryCommand
import logging
import re

class MockCommandHandler:
    """Mock class to simulate a command handler with history tracking."""
    
    def __init__(self):
        self.history = []

@pytest.fixture
def history_setup():
    """
    Fixture to set up a temporary history instance.
    Cleans up test files after execution.
    """
    command_handler = MockCommandHandler()
    history = HistoryCommand(command_handler, history_file="test_history.log", csv_file="test_history.csv")
    yield history
    os.remove("test_history.log") if os.path.exists("test_history.log") else None
    os.remove("test_history.csv") if os.path.exists("test_history.csv") else None

def test_add_history_entry(history_setup):
    """Test if a command is added to history properly."""
    history_setup.command_handler.history.append("add 2 3 = 5")
    assert len(history_setup.command_handler.history) == 1

def test_save_history(history_setup):
    """Test if history is saved to a CSV file correctly."""
    history_setup.command_handler.history.append("multiply 4 5 = 20")
    history_setup.save_history()
    assert os.path.exists("test_history.csv")

    df = pd.read_csv("test_history.csv")
    assert df.iloc[0]["Operation"] == "multiply"
    assert str(df.iloc[0]["Operand 1"]) == "4"
    assert str(df.iloc[0]["Operand 2"]) == "5"
    assert str(df.iloc[0]["Result"]) == "20"

def test_clear_history(history_setup):
    """Test clearing the history."""
    history_setup.command_handler.history.append("subtract 10 2 = 8")
    history_setup.clear_history()
    assert len(history_setup.command_handler.history) == 0
    assert os.path.exists("test_history.csv")

def test_delete_history_entry(history_setup):
    """Test deleting a history entry by index."""
    history_setup.command_handler.history.append("divide 10 2 = 5")
    history_setup.delete_history_entry(0)
    assert len(history_setup.command_handler.history) == 0

def test_delete_invalid_entry(history_setup, capsys):
    """Test attempting to delete a non-existent entry."""
    history_setup.delete_history_entry(5)  # Should print "Invalid index."
    captured = capsys.readouterr()
    assert "Invalid index." in captured.out

def test_save_empty_history(history_setup):
    """Test saving when there are no history entries."""
    history_setup.clear_history()
    history_setup.save_history()

    df = pd.read_csv("test_history.csv")

    assert df.empty  # Ensure the DataFrame has no rows
    assert list(df.columns) == ["No.", "Operation", "Operand 1", "Operand 2", "Result"]

def test_show_empty_history(history_setup, capsys):
    """Test displaying history when empty."""
    history_setup.clear_history()
    history_setup.show_history()
    captured = capsys.readouterr()
    assert "No command history found." in captured.out

def test_load_history(history_setup):
    """Test loading history from a file."""
    history_setup.command_handler.history.append("add 3 2 = 5")
    history_setup.save_history()

    # Create a new instance to check if it loads correctly
    new_history = HistoryCommand(MockCommandHandler(), history_file="test_history.csv")
    assert len(new_history.command_handler.history) > 0

def test_execute_show(history_setup, capsys):
    """Test execute command with 'show' argument."""
    history_setup.command_handler.history.append("multiply 2 3 = 6")
    history_setup.execute("show")
    captured = capsys.readouterr()
    assert "multiply 2 3 = 6" in captured.out

def test_execute_clear(history_setup):
    """Test execute command with 'clear' argument."""
    history_setup.command_handler.history.append("subtract 5 1 = 4")
    history_setup.execute("clear")
    assert len(history_setup.command_handler.history) == 0

def test_execute_save(history_setup):
    """Test execute command with 'save' argument."""
    history_setup.command_handler.history.append("add 10 5 = 15")
    history_setup.execute("save")
    assert os.path.exists("test_history.csv")

def test_execute_show(history_setup, capsys):
    """Test execute command with 'show' argument."""
    history_setup.command_handler.history.append("multiply 2 3 = 6")
    history_setup.execute("show")
    captured = capsys.readouterr()

    # Normalize captured output (remove tabulation, extract key values)
    output = re.sub(r'\s+', ' ', captured.out)  # Replace multiple spaces with a single space

    # Check if key values exist in output
    assert "multiply" in output
    assert "2" in output
    assert "3" in output
    assert "6" in output
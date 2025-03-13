"""
Unit tests for the HistoryCommand class.
"""

import os
import pytest
import pandas as pd
from app.plugins.history import HistoryCommand

class MockCommandHandler:
    """Mock class to simulate a command handler with history tracking."""
    
    def __init__(self):
        self.history = []

    def add_entry(self, entry):
        """Adds an entry to history."""
        self.history.append(entry)

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

    # Verify the contents
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

def test_delete_invalid_entry(history_setup):
    """Test attempting to delete a non-existent entry."""
    history_setup.delete_history_entry(5)  # Should print "Invalid index."

def test_save_empty_history(history_setup):
    """Test saving when there are no history entries."""
    history_setup.clear_history()
    history_setup.save_history()

    # Read the CSV file safely
    df = pd.read_csv("test_history.csv")

    # Ensure the CSV file contains headers but no data
    assert df.empty  # Check if the DataFrame has no rows
    assert list(df.columns) == ["No.", "Operation", "Operand 1", "Operand 2", "Result"]


def test_show_empty_history(history_setup):
    """Test displaying history when empty."""
    history_setup.clear_history()
    assert len(history_setup.command_handler.history) == 0

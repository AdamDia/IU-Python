import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.data_processor import select_ideal_functions

import pandas as pd
print("DEBUG: Importing select_ideal_functions...")
from src.data_processor import select_ideal_functions
print("DEBUG: Import successful!")

def test_select_ideal_functions():
    """
    Test selecting ideal functions based on least squares.
    """
    # Mock training data
    training_data = pd.DataFrame({
        'X': [1, 2, 3],
        'Y1': [2.0, 3.0, 4.0],
        'Y2': [5.0, 6.0, 7.0],
    })

    # Mock ideal functions
    ideal_functions = pd.DataFrame({
        'X': [1, 2, 3],
        'Y1': [2.0, 3.0, 4.0],
        'Y2': [5.1, 6.1, 7.1],
    })

    # Call the function
    best_fit = select_ideal_functions(training_data, ideal_functions)

    # Assertions
    assert best_fit == {'Y1': 'Y1', 'Y2': 'Y2'}

def test_process_data():
    """
    Test process_data to ensure training and ideal function data are generated.
    """
    from sqlalchemy import create_engine
    from src.data_processor import process_data

    # Use an in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')

    # Call process_data
    training_data, ideal_functions = process_data(engine)

    # Assertions
    assert len(training_data) > 0
    assert len(ideal_functions) > 0
    assert 'X' in training_data.columns
    assert 'Y1' in ideal_functions.columns

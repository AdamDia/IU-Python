import pandas as pd

def process_data(engine):
    """
    Loads training and ideal function data from CSVs and inserts them into the database.

    Args:
        engine: SQLAlchemy database engine.

    Returns:
        Tuple of training data and ideal functions as Pandas DataFrames.
    """
    training_data = pd.read_csv('data/training.csv')
    ideal_functions = pd.read_csv('data/ideal_functions.csv')

    # Store into the database
    training_data.to_sql('training_data', engine, if_exists='replace', index=False)
    ideal_functions.to_sql('ideal_functions', engine, if_exists='replace', index=False)

    return training_data, ideal_functions

import pandas as pd

def process_data(engine):
    """
    Generates & Loads training and ideal function data from CSVs and inserts them into the database.

    Args:
        engine: SQLAlchemy database engine.

    Returns:
        Tuple of training data and ideal functions as Pandas DataFrames.
    """
    # Generate training data
    training_data = pd.DataFrame({
        'X': [1, 2, 3, 4],
        'Y1': [2.1, 3.1, 4.1, 5.1],
        'Y2': [3.5, 4.5, 5.5, 6.5],
        'Y3': [4.2, 5.2, 6.2, 7.2],
        'Y4': [5.3, 6.3, 7.3, 8.3],
    })
    training_data.to_csv('data/training.csv', index=False)

    # Generate ideal functions
    ideal_functions = {
        'X': [1, 2, 3, 4],
    }
    for i in range(1, 51):
        ideal_functions[f'Y{i}'] = [2.0 + i, 3.0 + i, 4.0 + i, 5.0 + i]
    ideal_functions_df = pd.DataFrame(ideal_functions)
    ideal_functions_df.to_csv('data/ideal_functions.csv', index=False)

    # Insert into database
    training_data.to_sql('training_data', engine, if_exists='replace', index=False)
    ideal_functions_df.to_sql('ideal_functions', engine, if_exists='replace', index=False)

    return training_data, ideal_functions_df

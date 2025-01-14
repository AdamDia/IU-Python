import sys
from pathlib import Path

# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.database import setup_database
from src.data_processor import process_data
from src.visualizer import visualize_data

def main():
    print("Setting up the database...")
    db = setup_database()

    print("Processing data...")
    training_data, ideal_functions = process_data(db)

    print("Visualizing results...")
    visualize_data(training_data, ideal_functions)

if __name__ == "__main__":
    main()

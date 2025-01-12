from sqlalchemy import create_engine, Table, Column, Float, MetaData

def setup_database():
    engine = create_engine('sqlite:///project.db')
    metadata = MetaData()

    # Define training data table
    training_table = Table(
        'training_data', metadata,
        Column('X', Float, primary_key=True),
        Column('Y1', Float),
        Column('Y2', Float),
        Column('Y3', Float),
        Column('Y4', Float)
    )

    # Define ideal functions table
    ideal_table = Table(
        'ideal_functions', metadata,
        Column('X', Float, primary_key=True)
    )
    for i in range(1, 51):
        ideal_table.append_column(Column(f'Y{i}', Float))

    metadata.create_all(engine)
    return engine

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

def visualize_data(training_data, ideal_functions):
    """
    Visualizes the training data and ideal functions using Bokeh.

    Args:
        training_data
        ideal_functions
    """
    p = figure(title="Training Data vs Ideal Functions", x_axis_label='X', y_axis_label='Y')

    # Plot training data
    for col in training_data.columns[1:]:
        p.line(training_data['X'], training_data[col], legend_label=f"Training {col}")

    # Plot ideal functions
    for col in ideal_functions.columns[1:]:
        p.line(ideal_functions['X'], ideal_functions[col], line_dash="dotted", legend_label=f"Ideal {col}")

    show(p)

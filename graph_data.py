import matplotlib.pyplot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Assume the 'data' variable is your DataFrame with the relevant data.
# If you're starting from scratch, you would have something like this:
np.random.seed(42)  # For reproducibility
data = {
    'Extraversion': np.random.uniform(0, 100, 100),
    'Intuition': np.random.uniform(0, 100, 100),
    'Thinking': np.random.uniform(0, 100, 100),
    'Judging': np.random.uniform(0, 100, 100),
    'Grade Percentage': np.random.uniform(0, 100, 100)
}

df = pd.DataFrame(data)

# Create a PairGrid object with the DataFrame
g = sns.PairGrid(df, vars=['Extraversion', 'Intuition', 'Thinking', 'Judging', 'Grade Percentage'])

# Map the plots to the lower and upper triangle of the grid
g.map_upper(sns.scatterplot, alpha=0.5)
g.map_lower(sns.scatterplot, alpha=0.5)


# Replace the diagonal plots with labels
def label_diag(ax, label):
    ax.set_axis_off()
    ax.annotate(label, xy=(0.5, 0.5), xycoords='axes fraction', ha='center', va='center', fontsize=12)


# Use the label_diag function for the diagonals
labels = ['Extraversion', 'Intuition', 'Thinking', 'Judging', 'Grade Percentage']
for i, ax in enumerate(np.diag(g.axes)):
    label_diag(ax, label=labels[i])

# Show the plot
plt.show()

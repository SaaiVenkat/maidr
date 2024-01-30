import seaborn as sns
import matplotlib.pyplot as plt
import json

# Load the iris dataset
iris = sns.load_dataset('iris')

# Set the size of the figure
plt.figure(figsize=(10, 6))

# Create a scatter plot of sepal length vs petal length
sns.scatterplot(x='sepal_length', y='petal_length', data=iris, label='Individual Measurements')

# Overlay a regression line
regline = sns.regplot(x='sepal_length', y='petal_length', data=iris, scatter=False, color='red', label='Regression Line', lowess=True)

# Extract scatter plot data
scatter_data = [{'x': row['sepal_length'], 'y': row['petal_length']} for index, row in iris.iterrows()]

# Extracting the line data
line_data = regline.get_lines()[0].get_data()
regression_data = [{'x': x, 'y': y} for x, y in zip(line_data[0], line_data[1])]

# Enhancing the plot
plt.title('Iris Sepal Length vs Petal Length with Regression Line')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()

# Save the plot as an SVG file
plt.savefig('scatterplot_point_smooth.svg', format='svg')

# Generating the 'maidr' structure for the 'Adelie' species
maidr = {
    'type': ['point', 'smooth'],
    'id': 'scatter',
    'selector': [
        "TODO: INCLUDE THE POINT SELECTOR HERE",
        "TODO: INCLUDE THE SMOOTH SELECTOR HERE"
    ],
    'title': 'Iris Sepal Length vs Petal Length with Regression Line',
    'name': 'Iris Plot',
    'axes': {
        'x': {
            'label': 'Sepal Length (cm)',
        },
        'y': {
            'label': 'Petal Length (cm)',
        },
    },
    'labels': {
        'title': 'Iris Sepal Length vs Petal Length with Regression Line',
        'x': 'Sepal Length (cm)',
        'y': 'Petal Length (cm)',
    },
    'data': [
        # scatter plot
        scatter_data,

        # regression line
        regression_data
    ],
}

# Writing the raw data to a JSON file
with open("scatterplot_point_smooth_raw_data.json", 'w') as json_file:
    json.dump(maidr["data"], json_file, indent=4)

# Writing the dictionary to a JSON file
with open("scatterplot_point_smooth_maidr.json", 'w') as json_file:
    json.dump(maidr, json_file, indent=4)

# Show the plot
plt.show()

# Close the plot
plt.close()

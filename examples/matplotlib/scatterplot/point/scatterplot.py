import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json

# Load an example dataset from seaborn
data = sns.load_dataset('penguins')

# Create a scatter plot with the seaborn dataset
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=data, x="bill_length_mm", y="bill_depth_mm", hue="species", style="species", palette="deep")
plt.title('Penguin bill dimensions by species')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')

# Save the plot as an SVG file
plt.savefig('scatterplot.svg', format='svg')

# Generating the 'maidr' structure
maidr = {
    'type': 'point',
    'id': 'scatter',
    'selector': "TODO: INCLUDE THE POINT SELECTOR HERE",
    'title': 'Penguin bill dimensions by species',
    'name': 'Scatterplot',
    'axes': {
        'x': {
            'label': 'Bill Length (mm)',
        },
        'y': {
            'label': 'Bill Depth (mm)',
        },
    },
    'labels': {
        'title': 'Penguin bill dimensions by species',
        'x': 'Bill Length (mm)',
        'y': 'Bill Depth (mm)',
    },
    'data': [
        [
            {
                'x': row['bill_length_mm'],
                'y': row['bill_depth_mm'],
            }
            for _, row in data.iterrows() if not (pd.isnull(row['bill_length_mm']) or pd.isnull(row['bill_depth_mm']))
        ]
    ],
}

# Writing the raw data to a JSON file
with open("scatterplot_raw_data.json", 'w') as json_file:
    json.dump(maidr["data"], json_file, indent=4)

# Writing the dictionary to a JSON file
with open("scatterplot_maidr.json", 'w') as json_file:
    json.dump(maidr, json_file, indent=4)   

# Display the plot
plt.show()

# Close the plot
plt.close()

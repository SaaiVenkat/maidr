import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset('iris')

# Set the size of the figure
plt.figure(figsize=(10, 6))

# Create a scatter plot of sepal length vs petal length
sns.scatterplot(x='sepal_length', y='petal_length', data=iris, label='Individual Measurements')

# Overlay a regression line
# sns.regplot(x='sepal_length', y='petal_length', data=iris, scatter=False, color='red', label='Regression Line', lowess=True)

# Enhancing the plot
plt.title('Iris Sepal Length vs Petal Length with Regression Line')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()

# Save the plot as an SVG file
plt.savefig('scatterplot2.svg', format='svg')

# Show the plot
plt.show()

# Close the plot
plt.close()
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame

df = pd.read_csv('cleaned_bank.csv')

# Group the data by 'Geography' and count the number of customers in each category
geography_counts = df['Geography'].value_counts()

# Create a pie chart
#plt.figure(figsize=(8, 8))
plt.pie(geography_counts, labels=geography_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Customers by Geography')

# Display the pie chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.savefig('geography_pie_chart.png')
plt.show()



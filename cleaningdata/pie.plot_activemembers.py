import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame

df = pd.read_csv('cleaned_bank.csv')

# Count the number of active and inactive members
active_members = df[df['IsActiveMember'] == 1]['CustomerId'].count()
inactive_members = df[df['IsActiveMember'] == 0]['CustomerId'].count()

# Create a pie chart
labels = 'Active Members', 'Inactive Members'
sizes = [active_members, inactive_members]
colors = ['lightblue', 'lightcoral']
explode = (0.1, 0)  # Explode the 1st slice (Active Members)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.title('Percentage of Active and Inactive Members')
plt.savefig('customerbypercent.png')
plt.show()







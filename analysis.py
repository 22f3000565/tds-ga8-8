import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
mrr = [2.16, 5.57, 12.55, 8.27]
industry_target = 15
average_mrr = 7.14

# Create the figure and axes
fig, ax = plt.subplots()

# Create the bar chart
ax.bar(quarters, mrr, label='Quarterly MRR')

# Add the industry target line
ax.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target')

# Add the average line
ax.axhline(y=average_mrr, color='g', linestyle='-', label='Average MRR')


# Add labels and title
ax.set_ylabel('MRR ($M)')
ax.set_title('Quarterly MRR Performance vs. Industry Target')
ax.legend()

# Save the chart
plt.savefig('chart.png')

print("Chart saved as chart.png")

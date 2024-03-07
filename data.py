import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('games.csv')

opening_counts = df['opening_name'].value_counts()

# Select the top 10 most popular openings
best_openings = opening_counts.head(10)

# Select the top 10 least popular openings
worst_openings = opening_counts.tail(10)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
best_openings.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Popular Opening Moves')
plt.xlabel('Opening Move')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.subplot(1, 2, 2)
worst_openings.plot(kind='bar', color='salmon')
plt.title('Top 10 Leat Popular Opening Moves')
plt.xlabel('Opening Move')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()

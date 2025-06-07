import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV file
data = pd.read_csv("C:\\Users\\Krishnendu\\Krishnendu\\DiwaliSalesData.csv",  encoding='windows-1252')

# Bar chart
plt.figure(figsize=(6, 4))
sns.countplot(x='Gender', data=data)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(6, 4))
sns.histplot(data['Age'], bins=10, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

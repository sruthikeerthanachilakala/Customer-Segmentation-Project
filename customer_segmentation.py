import kagglehub
import pandas as pd
import os

# Download the dataset
path = kagglehub.dataset_download("shwetabh123/mall-customers")

print("Dataset downloaded to:", path)

# Show files in the dataset folder
print("Files:", os.listdir(path))

# Load the CSV file
csv_file = os.listdir(path)[0]
df = pd.read_csv(os.path.join(path, csv_file))

# Display the first 5 rows
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nSummary Statistics:")
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# Scatter Plot
plt.figure(figsize=(8,6))
sns.scatterplot(
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    data=df
)

plt.title("Customer Distribution")
plt.savefig("customer_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

from sklearn.cluster import KMeans

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.savefig("elbow_method.png", dpi=300, bbox_inches="tight")
plt.show()

# Apply K-Means with 5 clusters
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)

df['Cluster'] = kmeans.fit_predict(X)

print(df.head())

plt.figure(figsize=(10, 7))

plt.scatter(
    df['Annual Income (k$)'],
    df['Spending Score (1-100)'],
    c=df['Cluster'],
    cmap='viridis',
    s=80
)

# Plot cluster centers
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    color='red',
    marker='X',
    s=250,
    label='Centroids'
)

plt.title("Customer Segmentation using K-Means")
plt.legend()
plt.savefig("customer_segments.png", dpi=300, bbox_inches="tight")
plt.show()
print(df.groupby('Cluster').mean(numeric_only=True))

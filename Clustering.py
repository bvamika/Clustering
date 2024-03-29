# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f9VdUM7Sms2TjAphHQrkSkvMq1YEK1Jf
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = {
'Branch ID': ['BID001', 'BID002', 'BID003', 'BID004', 'BID005', 'BID006', 'BID007', 'BID008',
'BID009', 'BID010','BID011', 'BID012', 'BID013', 'BID014', 'BID015', 'BID016',
'BID017', 'BID018', 'BID019', 'BID020'],
'Employee': [5, 5, 5, 5, 6, 6, 7, 8, 8, 8, 9, 11, 12, 12, 13, 13, 17, 19, 19, 21],
'Location': ['Good', 'Excellent', 'Poor', 'Excellent', 'Poor', 'Excellent', 'Poor', 'Good', 'Excellent', 'Good','Excellent', 'Poor', 'Good', 'Excellent', 'Good', 'Poor', 'Good', 'Excellent', 'Good', 'Excellent'],
'Investment': [3146, 3152, 3307, 3466, 3933, 4074, 4190, 4945, 5456, 6743, 6850, 7101, 7343, 8844, 9095, 9200, 9315, 9508, 9521, 9521],
'Expenses': [21770, 25270, 27316, 27867, 28339, 29232, 30989, 37339, 37931, 39172, 42661, 43348, 43883, 43924, 44127, 44986, 45001, 45237, 46931, 46931],
'Sales': [146233, 148991, 157278, 209618, 218211, 237164, 239073, 273295, 275179, 289909, 305607, 311500, 341853, 351158, 383053, 388936, 450807, 470227, 476594, 476594]
}

df=pd.DataFrame(data)

# Selecting numerical columns for clustering
numerical_cols = ['Employee', 'Investment', 'Expenses', 'Sales']
X = df[numerical_cols]
# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform PCA to reduce dimensionality for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Determine the optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
  kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
  kmeans.fit(X_scaled)
  wcss.append(kmeans.inertia_)

# Plot the Elbow Method to find the optimal number of clusters
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.show()

# Based on the Elbow Method, let's choose k=3
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize the clusters in 2D using PCA
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['Cluster'], cmap='viridis')
plt.title('K-Means Clustering (k=3)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
# Print the DataFrame with assigned clusters
print(df[['Branch ID', 'Cluster']])


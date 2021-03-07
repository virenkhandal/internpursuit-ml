import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('fakeStudent.csv')

df['Problem Solving'] = df['Rank each skill on the list first to last. [Problem Solving]'].astype(str).str[0]
df['Creativity'] = df['Rank each skill on the list first to last. [Creativity]'].astype(str).str[0]
df['Research'] = df['Rank each skill on the list first to last. [Research]'].astype(str).str[0]
df['Time Management'] = df['Rank each skill on the list first to last. [Time Management]'].astype(str).str[0]
df['Communication'] = df['Rank each skill on the list first to last. [Communication]'].astype(str).str[0]
# df['Critical Thinking'] = df[' [Critical Thinking]'].astype(str).str[0]

newdf = df[['Problem Solving', 'Creativity', 'Research', 'Time Management', 'Communication']]
# print(newdf)

scaler = MinMaxScaler()
new_df = pd.DataFrame(scaler.fit_transform(newdf), columns=newdf.columns[:], index=newdf.index)

print(new_df)

from sklearn.decomposition import PCA

# Instantiating PCA
pca = PCA()

# Fitting and Transforming the DF
df_pca = pca.fit_transform(new_df)

# Plotting to determine how many features should the dataset be reduced to
plt.style.use("bmh")
plt.figure(figsize=(14,4))
plt.plot(range(1,new_df.shape[1]+1), pca.explained_variance_ratio_.cumsum())
plt.show()

# Finding the exact number of features that explain at least 95% of the variance in the dataset
total_explained_variance = pca.explained_variance_ratio_.cumsum()
n_over_95 = len(total_explained_variance[total_explained_variance>=.95])
n_to_reach_95 = new_df.shape[1] - n_over_95

# Printing out the number of features needed to retain 95% variance
print(f"Number features: {n_to_reach_95}\nTotal Variance Explained: {total_explained_variance[n_to_reach_95]}")

# Reducing the dataset to the number of features determined before
pca = PCA(n_components=n_to_reach_95)

# Fitting and transforming the dataset to the stated number of features and creating a new DF
df_pca = pca.fit_transform(new_df)

# Seeing the variance ratio that still remains after the dataset has been reduced
print(pca.explained_variance_ratio_.cumsum()[-1])



hac = AgglomerativeClustering(n_clusters=10)

# Fitting
hac.fit(df_pca)

# Getting cluster assignments
cluster_assignments = hac.labels_

# Unscaling the categories then replacing the scaled values
df = df[['Best email to reach you']].join(pd.DataFrame(scaler.inverse_transform(newdf), columns=newdf.columns[:], index=newdf.index))

# Assigning the clusters to each profile
df['Cluster #'] = cluster_assignments

# Viewing the dating profiles with cluster assignments
print(df)



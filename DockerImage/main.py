import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from requests import get
import json


# read data
ENDPOINT = "https://wine-data.onrender.com/wine"
response = get(ENDPOINT)
df_wine=pd.datos = pd.read_json(response.json())


# Calculate and print data exploration
print('')
print('')
print('DATASET EXPLORATION')
print('-----------------------')
print("Number of rows: " + str(df_wine.shape[0]))
print("Number of columns: " + str(df_wine.shape[1]))
print("Number of missing values: " + str(df_wine.isna().sum().sum()))


 # Print column pairs with correlation greater than 0.5
print('')
print("COLUMNS CORRELATED WITH COEFFICIENT GREATER THAN 0.5:")
print('-----------------------')

def calculate_and_show_correlation(df):
    # Calculate the correlation matrix
    correlation_matrix = df.corr('spearman')

    # Initialize a list to store the pairs (index, column, value)
    correlation_pairs = []

    # Iterate through the correlation matrix
    for index_row_1 in correlation_matrix.index:
        for index_column_1 in correlation_matrix.columns:
            correlation_value_1 = correlation_matrix.loc[index_row_1, index_column_1]

            # Evaluate the condition (greater than 0.5)
            if 0.5 < abs(correlation_value_1) < 1.0:

                # Check if a pair with the same elements already exists in the list
                pair_exists = False
                for pair in correlation_pairs:
                    index_row_2, index_column_2, correlation_value_2 = pair
                    if (index_row_1 == index_row_2 and index_column_1 == index_column_2) or \
                       (index_row_1 == index_column_2 and index_column_1 == index_row_2):
                        pair_exists = True
                        break

                # If there is no pair with the same elements, add to the list
                if not pair_exists:
                    correlation_pairs.append([index_row_1, index_column_1, correlation_value_1])

    # Print the correlation pairs
    for pair in correlation_pairs:
        print(f"{pair[0]} - {pair[1]}: {pair[2]}")

calculate_and_show_correlation(df_wine)


print('')
print("MODELO CLUSTERING KMEANS")
print('-----------------------')

#Data Scaling
scaler=StandardScaler()
X=scaler.fit_transform(df_wine)

# Kmeans clustering model
k = 3
km = KMeans(n_clusters=k, random_state=0)
km.fit(X)
df_wine_label = df_wine.copy()

# Add a new column 'Cluster' to the original DataFrame
labels_kmeans = km.labels_
df_wine_label['Cluster'] = labels_kmeans 
df_wine_label_grouped = df_wine_label.groupby('Cluster').mean().round(2)
dictionaries_per_row = [dict(zip(df_wine_label_grouped.columns, row)) for _, row in df_wine_label_grouped.iterrows()]

# Print the dictionaries
print('AVERAGE CHARACTERISTICS OF EACH CLUSTER')
n = -1
for dictionary in dictionaries_per_row:
    n = n + 1
    print('cluster', n)
    print(dictionary)



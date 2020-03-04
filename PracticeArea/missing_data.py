# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Datasets/Data.csv')

print(dataset)
print(dataset.isnull().sum())

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

print(X)
print(y)

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values ='NaN', strategy ='mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)
import pandas as pd
import numpy as np

data=pd.read_csv('Datasets\Kidney.csv',header=None,names=['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu', 'sc', 'sod', 'pot', 
 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane', 'class'])
#print(data.head())
data.replace('?',np.NAN,inplace=True)
#print(data.isnull().sum())
#print(data.isnull().sum()/len(data))

num_cols = ['age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc']

# categorical columns
cate_cols = data.columns.drop('class').drop(num_cols)
# display categorical columns
#cate_cols

# convert numerical data 
data[num_cols] = data[num_cols].apply(pd.to_numeric, errors='coerce')

# df info
data.info()

## Categorical boolean mask
categorical_feature_mask = (data.dtypes==object)

## filter categorical columns using mask and turn it into a list
categorical_cols = data.columns[categorical_feature_mask].tolist()

## show categorical columns
#print(categorical_cols)

# check the number of unique values



#print(data['dm'].unique())
#print(data['dm'].dtype)
data['dm'] = data['dm'].str.strip()
#print(data['dm'].unique())

data['class']=data['class'].apply(lambda x: 1 if x=='ckd' else 0)

print(data['class'].head())

X=data.drop(columns=['class'])
Y=data['class']


from sklearn.preprocessing import Imputer

# define numerical imputer
num_Imputer=Imputer(strategy='mean')
# imputing on numerical data
X[num_cols]=num_Imputer.fit_transform(X[num_cols])


from sklearn_pandas import  CategoricalImputer
from PracticeArea.fill_missing_values import Categorical_Imputer
from PracticeArea.missing_values_table import missing_values_table

#cate_imputer = CategoricalImputer('most_frequent')
#X[cate_cols] = cate_imputer.fit_transform(X[cate_cols])

cate_imputer = Categorical_Imputer('most_frequent')
X[cate_cols] = cate_imputer.fit_transform(X[cate_cols])
#print(X.isnull().sum())

#cate_imputer1 = CategoricalImputer(strategy='most_frequent')
#X[cate_cols] = X[cate_cols].apply(lambda x: cate_imputer1.fit_transform(x), axis='columns')
#print(X.isnull().sum())

#missing_values_table(X)
#print(X['htn'].unique())
#print(pd.get_dummies(X['rbc'], prefix_sep='_'))

# Get dummies
#X = pd.get_dummies(X,columns=['htn'], prefix_sep='_', drop_first=True)
X = pd.get_dummies(X, prefix_sep='_', drop_first=True)
## X head
print(X.head())

# XGB
#import xgboost as xgb
# cross_val_score
from sklearn.model_selection import cross_val_score






















from sklearn_pandas import CategoricalImputer
import pandas as pd


class Categorical_Imputer: 
    
  
    def __init__(self, strategy):
        self.strategy = strategy
        

    def fit_transform(self, df:'dataframe'):      
        imputer = CategoricalImputer()
        df_filled = df.apply(lambda x: imputer.fit_transform(x), axis=0) 
        return df_filled
        
        
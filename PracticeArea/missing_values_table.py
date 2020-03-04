
import pandas as pd

def missing_values_table(df):
   

    mis_val = df.isnull().sum()
    

    mis_val_percent = 100 * df.isnull().sum() / len(df)
   
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    

    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    

    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
    '% of Total Values', ascending=False).round(2) 
    
 
    print("Your slelected dataframe has {} columns.".format(df.shape[1]) + '\n' + 
    "There are {} columns that have missing values.".format(mis_val_table_ren_columns.shape[0]))
    
    
    return mis_val_table_ren_columns
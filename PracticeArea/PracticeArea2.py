import pandas as pd
import os

#print(os.getcwd())

data=pd.read_csv("Datasets\pacific.csv",header=0)
##data.drop("Name",axis=1,inplace=True)
#print(data.head(6))
#print(data['Status'])

#data.filter(items=['Name', 'Status'])
###data.drop("ElderlyPop",axis=1,inplace=True)
##print(data["Status"].unique())
##data1=data.groupby(data["Status"]).size()
##print(data1)
#data2=data[data['Status'] == 'TS']
#print(data2.head())

#print(data)

gapminder_2002 = data[data['Status']==" TS"]
print(gapminder_2002)


#data3=data.filter(like='HU', axis=0)
#print(data3)


#' TS' ' HU' ' TD' ' EX' ' LO' ' ET' ' DB' ' SD' ' SS' ' PT' ' ST' ' HU '

#data.Status = pd.Categorical(data.Status)
#data['Status'] = data.Status.cat.codes
#print(data.head())



#print(data.head(6))





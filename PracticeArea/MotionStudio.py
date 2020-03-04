#MOTION STUDIO
#Domain: Media
#Focus: Optimize Selection Process

#Business Challenge: Motion Studio is the largest Radio production house in Europe. Having a revenue of more than a Billion Dollars, the company has decided to launch a new reality show: RJ Star. Response to the show is unprecedented and the company is flooded with voice clips. You as an ML expert have to classify the voice as either male/female so that the first level of filtration is quicker.

#Key Issues: Voice sample are across accents.

#Business Benefit: Since RJ Star is a reality show, time to select candidates is very short. The whole success of the show and hence the profits depends upon quick and smooth execution

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import warnings
#warnings.filterwarnings('ignore') 

df = pd.read_csv('Datasets\classificationvoice.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print ( "Shape of Data:" , df.shape)
print("Total number of labels: {}".format(df.shape[0]))
print("Number of male: {}".format(df[df.label == 'male'].shape[0]))
print("Number of female: {}".format(df[df.label == 'female'].shape[0]))

X=df.iloc[:, :-1]
print (df.shape)
print (X.shape)

from sklearn.preprocessing import LabelEncoder
y=df.iloc[:,-1]
 
gender_encoder = LabelEncoder()
y = gender_encoder.fit_transform(y)
print("Label Encoder :",y)
 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
print("Standard Scaler :",X)
 


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
 
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix
 
svc_model=SVC()
svc_model.fit(X_train,y_train)
y_pred=svc_model.predict(X_test)

print(y_pred)
 
print('Accuracy Score:')
print(metrics.accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))



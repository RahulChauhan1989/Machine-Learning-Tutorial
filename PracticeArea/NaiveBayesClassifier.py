
# Step 1 - Load data
import pandas as pd

data=pd.read_csv("Datasets/iphone_purchase_records.csv")
X=data.iloc[:,:-1].values
Y=data.iloc[:,3].values

# Step 2 - Convert Gender to number
from sklearn.preprocessing import LabelEncoder
labelEncoder_gender=LabelEncoder()
X[:,0]=labelEncoder_gender.fit_transform(X[:,0])

# Optional - if you want to convert X to float data type
import numpy as np
X=np.vstack(X[:,:]).astype(np.float)

# Step 3 - Splitting the data into Train and Test
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

# Step 4 - Feature Scaling
from sklearn.preprocessing import StandardScaler
ss_X = StandardScaler()
X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)


# Step 5 - Fit the classifier
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,Y_train)

# Step 6 - Predict
predict=classifier.predict(X_test)

# Step 7 - Confusion Matrix
from sklearn import metrics
cm=metrics.confusion_matrix(Y_test,predict)
print(cm)
accuracy=metrics.accuracy_score(Y_test,predict)
print("Accuracy Score: ",accuracy)
precision=metrics.precision_score(Y_test,predict)
print("Precision Score: ",precision)
recall=metrics.recall_score(Y_test,predict)
print("Recall score:",recall)


#print(X)
#print(Y)
#print(data.head())
import numpy
import pandas as pnds
import matplotlib
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
data = pnds.read_csv("G:/Gender-Classification-master/500_Person_Gender_Height_Weight_Index.csv")
# if(not(bool(data.isnull().sum()))):


x = data.iloc[:, 1:3].values
y = data.iloc[:, 0].values

le = LabelEncoder()
# y = le.fit_transform(y)
# print(y)
clf = DecisionTreeClassifier()
clf.fit(x, y)
data.tail() #Last 5 data
data.head() #First 5 data
print(clf.predict([[155,70]]))


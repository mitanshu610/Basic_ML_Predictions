
# load the iris dataset 
from sklearn.model_selection import train_test_split
import pandas as pnds
from sklearn.preprocessing import LabelEncoder

data = pnds.read_csv("iris.csv")
# store the feature matrix (X) and response vector (y) 
iris_data = data.iloc[:, 0:4].values
iris_target = data.iloc[:, 4].values

le = LabelEncoder()
iris_target = le.fit_transform(iris_target)
# splitting X and y into training and testing sets

iris_data_train, iris_data_test, iris_target_train, iris_target_test = train_test_split(iris_data, iris_target, test_size=0.4, random_state=1)

# training the model on training set 
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(iris_data_train, iris_target_train)

# making predictions on the testing set 
prediction = gnb.predict([[5.4,3.5,1.4,0.2]])

print(prediction)
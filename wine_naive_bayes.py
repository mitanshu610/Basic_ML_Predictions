from sklearn.naive_bayes import GaussianNB
import pandas as pnds

# loading the wine data
data = pnds.read_csv("wine.csv")

# getting data and targets
wine_data = data.iloc[: , 1:14].values
wine_target = data.iloc[: , 0].values   # target contains the class of the wine 1,2,3

# print(wine_data)
# print(wine_target)
# encoding the wine target data
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
wine_target = le.fit_transform(wine_target)


#splitting the test and training data
from sklearn.model_selection import train_test_split
wine_data_train, wine_data_test, wine_target_train, wine_target_test = train_test_split(wine_data, wine_target, test_size=0.4, random_state=1)


#creating the model
wine_model = GaussianNB()
wine_model.fit(wine_data_train,wine_target_train) # fit the wine_date to the class of wine
prediction = wine_model.predict(wine_data_test)  # prediction of the wine test data

print(prediction)

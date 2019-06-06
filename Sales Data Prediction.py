import pandas as pnds
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
Sales_data = pnds.read_csv("G:\Sales-Data-Analysis-master\Advertising.csv")

x = Sales_data.iloc[:,1:4].values
y = Sales_data.iloc[:,4].values
# print(x)
# print(y)
tv = float(input("Enter the value of TV sales : "))
radio = float(input("Enter the value of Radio sales : "))
newspaper = float(input("Enter the value of Newspaper sales : "))

#here no label encoding is necessary as it is based on regression and not on classification
LReg = LinearRegression()
LReg.fit(x,y)
print(LReg.predict([[tv,radio,newspaper]]))
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5) #50% data goes to training and 50% goes to testing module
print(LReg.score(x_train,y_train))  
print(LReg.score(x_test,x_test))
# print(LReg.score(x,y))
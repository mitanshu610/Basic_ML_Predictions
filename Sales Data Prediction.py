import pandas as pnds
from sklearn.linear_model import LinearRegression
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
# print(LReg.score(x,y))
import numpy as np
X = np.array([[1,2,3],[4,5,6],[7,8,9]])
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])
import re
a = '[a-e]'
data = '2233az'
x = re.findall(a,data)
print(x) 
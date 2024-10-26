import matplotlib as plt
import pandas as pd 

iris = pd.read_csv("C:/data-csv/iris.csv", names = ['sepal_length','sepal_width','petal_length','class'])
print(iris.head())
print(iris.tail())

import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LinearRegression
data= pd.read_csv('data.csv')   
data.hist()
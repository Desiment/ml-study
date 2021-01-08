import pandas as pd
import numpy as np
import sklearn.linear_model as lm

data = pd.read_csv("../data/clear_data.csv")
X = data[["Median age", "Sex-ratio", "Urbanization rate"]]
Y = data["rfactor"]

reg = lm.LinearRegression(fit_intercept=True)
reg.fit(X, Y)






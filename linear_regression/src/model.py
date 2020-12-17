import pandas as pd
import numpy as np
import sklearn.linear_model as lm

import matplotlib.pyplot as plt

data = pd.read_csv("data/clear_data.csv")
X = data[["Median age", "Sex-ratio", "Urbanization rate"]]
Y = data["rfactor"]

reg = lm.LinearRegression()
reg.fit(X, Y)

#print(skm.score(X, Y))
#print(reg.coef_)

fig, (MA, SR, UR) = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))

MA.scatter(X["Median age"].tolist(), Y.tolist(), marker='o', c='b', edgecolor='k')
MA.set_title('Scatter: Median age versus $r$')
MA.set_xlabel('Median age')
MA.set_ylabel('$r$')

SR.scatter(X["Median age"].tolist(), Y.tolist(), marker='o', c='b', edgecolor='k')
SR.set_title('Scatter: Median age versus $r$')
SR.set_xlabel('Median age')
SR.set_ylabel('$r$')

UR.scatter(X["Median age"].tolist(), Y.tolist(), marker='o', c='b', edgecolor='k')
UR.set_title('Scatter: Median age versus $r$')
UR.set_xlabel('Median age')
UR.set_ylabel('$r$')

plt.savefig("ex.png")
# Predict:


import pandas as pd
import numpy as np
import sklearn.linear_model as lm

import matplotlib.pyplot as plt

data = pd.read_csv("../data/analyziz_prepared_data.csv")
X = data[["Median age", "Sex-ratio", "Urbanization rate"]]
Y = data["rfactor"]

reg = lm.LinearRegression(fit_intercept=True)
reg.fit(X, Y)

print(reg.score(X, Y))
print(reg.coef_)
print(reg.intercept_)

fig, (MA, SR, UR) = plt.subplots(nrows=1, ncols=3, figsize=(16, 8))
MA.plot([0, 1], [reg.intercept_, reg.intercept_ + reg.coef_[0]], c='r')
MA.scatter(X["Median age"].tolist(), Y.tolist(), marker='o', c='b', edgecolor='k')
MA.set_title('Scatter: Median age versus $r$')
MA.set_xlabel('Median age')
MA.set_ylabel('$r$')


SR.scatter(X["Sex-ratio"].tolist(), Y.tolist(), marker='o', c='b', edgecolor='k')
SR.plot([0, 0.2], [reg.intercept_, reg.intercept_ + 0.2*reg.coef_[1]], c='r')
SR.set_title('Scatter: Sex-ratio versus $r$')
SR.set_xlabel('Sex-ratio')
SR.set_ylabel('$r$')

UR.scatter(X["Urbanization rate"].tolist(), Y.tolist(), marker='o', c='b', edgecolor='k')
UR.plot([0, 1], [reg.intercept_, reg.intercept_ + reg.coef_[2]], c='r')
UR.set_title('Scatter: Urbanization rate versus $r$')
UR.set_xlabel('U. rate ')
UR.set_ylabel('$r$')

plt.savefig("ex.png")


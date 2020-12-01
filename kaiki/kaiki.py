import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pd.read_csv('sample.csv')
print(df)
x = df[['x']]
y = df[['y']]
model_lr = LinearRegression()
model_lr.fit(x,y)

print('y= %.3fx + %.3f' % (model_lr.coef_ , model_lr.intercept_))
print('決定係数 R^2: ', model_lr.score(x, y))

x = sm.add_constant(x)
model = sm.OLS(y, x)
res = model.fit()
print(res.summary())

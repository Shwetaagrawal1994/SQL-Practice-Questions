import numpy as np

X = 2*np.random.rand(100, 1)
y = 4 + 3*X + np.random.rand(100, 1) # shape is (100,1)
X_b = np.c_[ np.ones((100, 1)), X] # shape is (100,2)

# Estimating coefficients (Slope and intercept)
betas = np.linalg.inv(X_b.T.dot(X_b) ).dot(X_b.T).dot(y)
print(betas)

# Predictions
X_new = np.array([[0], [2]]) # creating numpy array with specific values
print(X_new)
X_test = np.c_[np.ones((2, 1)), X_new]
predict_Y = np.dot(X_test, betas)
print(predict_Y)

# Plot the predictions
# plt.plot(X_new, predict_Y, "r-")
# plt.plot(X, y, "b.")
# plt.axis([0, 2, 0, 15])
# plt.show()

# Linear Regression using scikit learn
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression
lin_reg.fit(X, y) # note that X with ones are not provided rather X has been provided
lin_reg.intercept_, lin_reg.reg_coef_
lin_reg.predict(X_new)
import numpy as np

print("---------------BATCH GRADIENT DESCENT STARTS ----------------")

print("***** BATCH GRADIENT DESCENT from scratch *****")
# Define predictors and response variables
X = 2*np.random.rand(100,1)
y = 4 + 3*X + np.random.randn(100,1)
X_b = np.c_[np.ones((100, 1)), X]

# Define parameters variables
eta = 0.1
n_iterations = 1000

# Define weights
w = np.random.rand(2, 1)

# Define batch gradient descent function
X_shape, Y_shape = np.shape(X_b)
# print(X_b.dot(w)) # how can this work when shapes are not alugned

# breakpoint()
for iter in range(n_iterations):
    
    gradients = 2/X_shape *X_b.T.dot(X_b.dot(w) - y)

    # print(np.shape(gradients))
    # updating weights
    w = w - eta * gradients

print(w)

########### Define stochastic gradient descent function

print("---------------STOCHASTIC GRADIENT DESCENT STARTS ----------------")

print("***** STOCHASTIC GRADIENT DESCENT from scratch *****")
# Define parameters variables
n_iterations = 50
t0, t1 = 5, 50

# Define weights
w = np.random.rand(2, 1)

for iter in range(n_iterations):
    for i in range(X_shape):
        random_index = np.random.randint(X_shape)
        x_i = X_b[random_index:(random_index+1) ]
        y_i = y[random_index:(random_index+1) ]

        gradients = 2/X_shape *X_b.T.dot(X_b.dot(w) - y)

        # updating learning rate - eta
        eta = t0/ ( (n_iterations*X_shape + iter) + t1 ) 

        # updating weights
        w = w - eta * gradients

print(w)

print("***** STOCHASTIC GRADIENT DESCENT from Scikit Learn *****")
# Stochastic Regression using Scikit Learn

from sklearn.linear_model import SGDRegressor

stgd_reg = SGDRegressor( n_iter = 50, penalty = None, eta0 = 0.1)
stgd_reg.fit(X, y.ravel())

stgd_reg.intercept_, stgd_reg.coef_
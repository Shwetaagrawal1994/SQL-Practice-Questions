import numpy as np

Xvar = np.random.rand(4, 100)
Yvar = np.round( np.random.rand(1, 100) ) 

weight = np.random.rand(4, 1)
delta_weight = np.zeros((4,1))

b = 0.1
alpha = 0.0001
epoch = 1000

num_rows, num_cols = Xvar.shape
loss_at_epoch = []

for iter in range(epoch) :
    print(iter)

    # Fitting the linear reg equation
    z = np.dot(weight.T, Xvar) + b # shape is 1,100

    # Fitting the Logistic reg equation and predicting Y hat
    a = 1/(1 + np.exp(-z) ) # shape is 1,100

    # Calculating the accuracy of the prediction
    Loss = ( Yvar* np.log(a) + (1- Yvar)*np.log(1 - a) )  # shape is 1,100
    loss_at_epoch.append(np.sum(Loss) ) # to check later if loss is decreasing at each epoch

    # Gradient descent implement i.e. update parameters after each run
    dz = a - Yvar # shape is 1,100

    delta_weight = (1/num_rows) * ( np.dot( Xvar, dz.T ) ) # shape is 1,4
    delta_beta = (1/num_rows) * np.sum(dz) # shape is 1,1

    weight = weight - alpha*delta_weight # shape is 1,4
    b = b - alpha*delta_beta 


# final weight and b
print(weight)
print(b)
breakpoint()

print(loss_at_epoch)


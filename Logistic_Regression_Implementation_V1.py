import numpy as np

Xvar = np.random.rand(5, 100)
print(Xvar)

Yvar = np.round(np.random.rand(1,100) )
print(Yvar)

# weights = np.zeros((5,1))

weights = np.ones((5,1))
# b = np.ones(5,1) -- command + front slash
b = 1
alpha = 0.01

print(" X shape:")
print(Xvar.shape)

print(" w shape:" )
print(weights.shape)

z = np.dot(weights.T, Xvar) + b

print(z.shape)
a = 1/ (1 + np.exp(-z) )

print(" a shape:" )
print(a.shape)

print(" check on J calculation" )
print(Yvar * np.log(a) )

J = Yvar * np.log(a) + (1-Yvar) * np.log( 1 - a)
print(" j shape:" )
print(J.shape)

dz = a - Yvar
print(" dz shape:" )
print(dz.shape)


dw = np.zeros((5,1))

dw = (1/100) * np.dot(Xvar , dz.T)
print(" dw shape:" )
print(dw.shape)

db = (1/100)* np.sum(dz)
print(db)
print(" db shape:" )
print(db.shape)

breakpoint()
weights = weights - alpha * dw

print(weights)
b = b - alpha * db
print(b)
# for i in range(100):
    


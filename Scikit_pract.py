from sklearn.datasets import load_breast_cancer
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# print(type(load_breast_cancer()) )
cancer = load_breast_cancer()
print(cancer.keys() )

print(format(cancer.keys()) )
print(cancer.data.shape )

print(np.bincount(cancer.target) )
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data, cancer.target, stratify = cancer.target, random_state= 66)

print(KNeighborsClassifier(n_neighbors= 2).fit(X_train, Y_train))
# clf = 





# Classification performance evaluation metrics

# Importing Libraries
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

# Load dataset
# mnist = fetch_mldata('MNIST original')
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
# print(mnist)
# print(mnist.keys())
# dict_keys(['data', 'target', 'frame', 'categories', 'feature_names', 'target_names', 'DESCR', 'details', 'url'])
X, y = mnist["data"], mnist["target"]
print(X.shape, y.shape)

# Train - test split
# shuffle_index = np.random.permutation(70000)
# X, y = X[shuffle_index], y[shuffle_index]
# X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
X_train, X_test, y_train, y_test = train_test_split(mnist.data, mnist.target, stratify = mnist.target, random_state= 66)


# Shuffle the tarining examples
# shuffle_index = np.random.permutation(60000)
# print(shuffle_index) # output random numbers between 1 and 60000
# X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]

# Create target vectors - below code will return true if 5 is present otherwise false
y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)
# print(y_train_5)

# Train a binary classifier - "5 detector" using SGD classifier
print(X_train.shape, y_train_5.shape)
# print(y_train_5)
print(np.unique(y_train_5))
# sgd = SGDClassifier(random_state = 42)
# sgd.fit(X_train, y_train_5)

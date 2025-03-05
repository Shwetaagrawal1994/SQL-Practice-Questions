# ###################### Dataset = load_digits #######
# Date - 27Dec 2024
# Importing Libraries
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier

# Load dataset
digits = load_digits()
print(digits.keys())
# dict_keys(['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])
X, y = digits.data, digits.target
print(X.shape, y.shape)

# Define y
y = (digits.target == 9) # 9s detector
print(y)

# Train - test split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train a binary classifier
dummy_maj = DummyClassifier(strategy= 'most_frequent').fit(X_train, y_train)
print(np.unique(dummy_maj.predict(X_test)) )

print("Test score: ",  dummy_maj.score(X_test, y_test))
breakpoint()

# ###################### Dataset = cancer #######
# Date - 26Dec 2024

# Classification performance evaluation metrics

# Importing Libraries
from sklearn.datasets import load_breast_cancer
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, precision_recall_curve, roc_curve, roc_auc_score
import matplotlib.pyplot as plt 

# Load dataset
cancer = load_breast_cancer()
X, y = cancer["data"], cancer["target"]
print(X.shape, y.shape)


# Train - test split
shuffle_index = np.random.permutation(569)
X, y = X[shuffle_index], y[shuffle_index]
X_train, X_test, y_train, y_test = X[:450], X[450:], y[:450], y[450:]
print(np.unique(y_train))

# Train a binary classifier
sgd = SGDClassifier(random_state = 42)
sgd.fit(X_train, y_train)
print(sgd.predict(X_test))

# Performance measures - This gives accuracy score for each CV
CV_value = cross_val_score(sgd, X_train, y_train, cv = 3, scoring="accuracy")
print(CV_value)

# Confusion Matrix - This gives the predicted 0 and 1 for each Y
y_pred = cross_val_predict(sgd, X_train, y_train, cv = 3)
# print(y_pred)
print(confusion_matrix(y_train, y_pred))

# Pecision, Recall and F1 Score values
# print("Accuracy: ",  score(y_train, y_pred))
print("Precision: ",  precision_score(y_train, y_pred))
print("Recall: ",  recall_score(y_train, y_pred))
print("F1 Score: ",  f1_score(y_train, y_pred))

# Pecision - Recall (PR) curve
y_score = cross_val_predict(sgd, X_train, y_train, cv = 3, method="decision_function")
precisons, recalls, thresholds = precision_recall_curve(y_train, y_score)
# print(precisons)
def plot_PR_curve(precisons, recalls, thresholds):
    plt.plot(thresholds, precisons[:-1], "b--", label = "Precision")
    plt.plot(thresholds, recalls[:-1], "g-", label = "Recall")
    plt.xlabel("Threshold")
    plt.legend(loc = "upper left")
    plt.ylim([0,1])

plot_PR_curve(precisons, recalls, thresholds)
plt.show()

# ROC Curve and AUC scores
fpr, tpr, thresholds = roc_curve(y_train, y_score)
def plot_ROC_curve(fpr, tpr, label = None):
    plt.plot(fpr, tpr, linewidth = 2 , label = label)
    plt.plot([0, 1], [0,1], 'k--')
    plt.axis([0,1,0,1])
    plt.xlabel("FPR")
    plt.ylabel("TPR")


plot_ROC_curve(fpr, tpr)
plt.show()

print("ROC AUC: ",  roc_auc_score(y_train, y_score))



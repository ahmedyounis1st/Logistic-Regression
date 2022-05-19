# -*- coding: utf-8 -*-
"""logistic_regression_sklearn_multi_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_sYl2PBfst4uZgvXEsROQawKTakIeSPK
"""

from sklearn.linear_model import LogisticRegression

from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train_final = X_train.reshape((-1, 784))

X_test_final = X_test.reshape((-1, 784))

X_train_final =  X_train_final / 255
X_test_final =  X_test_final / 255

model = LogisticRegression()

model.fit(X_train_final, y_train)

y_pred = model.predict(X_test_final)
y_pred

from sklearn.metrics import accuracy_score
acc_score = accuracy_score(y_test, y_pred)*100
acc_score

import matplotlib.pyplot as plt
plt.imshow(X_test[5],cmap="gray")
print(y_pred[5])


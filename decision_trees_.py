# -*- coding: utf-8 -*-
"""Decision Trees .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rZNIXSQAlaESqr7C62G8ARLvVKtQCZnE
"""

import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
from matplotlib import pyplot as plt

!wget -O drug200.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv

DS = pd.read_csv("/content/drug200.csv" , delimiter=",")

DS.info

DS.columns
col = ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']

DS.head()

col_names = [ 'Sex', 'BP', 'Cholesterol', 'Drug']
for col in col_names:
    print(DS[col].value_counts())

print(DS["Drug"].value_counts())

x = DS[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
y = DS[["Drug"]].values

from sklearn.preprocessing import LabelEncoder
LE =LabelEncoder()
x[: , 1] = LE.fit_transform(x[: , 1 ])
x[: , 2] = LE.fit_transform(x[: , 2 ])
x[: , 3] = LE.fit_transform(x[: , 3 ])

from sklearn.model_selection import train_test_split
x_trainset, x_testset, y_trainset, y_testset = train_test_split(x, y, test_size=0.3, random_state=3)

from sklearn.tree import DecisionTreeClassifier
drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
drugTree.fit(x_trainset,y_trainset)

predTree = drugTree.predict(x_testset)
plt.hist(y_testset , color="r")

plt.hist(predTree , color="r")

from sklearn import metrics
import matplotlib.pyplot as plt
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))

plt.figure(figsize=(12,8) , facecolor="r"   )
from sklearn import tree
tree.plot_tree(DTC.fit(X_train, y_train) , fontsize=12 ,rounded=True ) 
plt.show()




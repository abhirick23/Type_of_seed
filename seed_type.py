# -*- coding: utf-8 -*-
"""Seed_type

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B9Xe6-pfhioBhBVQ74p86NUFA8Svr49m
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive/')
# %cd /gdrive

ls

cd /gdrive/MyDrive/Seed_type

ls

"""# Importing Libraries"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")
import joblib

"""# Uploading Dataset"""



df_train=pd.read_csv('Class_Seeds.csv')
df_train.head()

df_train.info()

df_train.describe().style.background_gradient(axis=0,cmap = 'RdYlGn')

"""# EDA"""

df_train.isna().sum()

df_train.columns

df_train.Class.value_counts()

columns = df_train.columns
binary_cols = []
remain_cols=[]
for col in columns:
    if df_train[col].value_counts().shape[0] == 2:
        binary_cols.append(col)
    else:
      remain_cols.append(col)

binary_cols

sns.countplot("Area", data=df_train)

sns.countplot("Compactness", data=df_train)

plt.figure(figsize=(12,9),dpi = 100)
sns.heatmap(df_train.corr(),vmax=.8,annot = True, square = True)
plt.show()

sns.set(rc={'figure.figsize':(11.7,8.27)})
cData_attr = df_train.iloc[:, 0:7]
sns.pairplot(cData_attr, diag_kind='kde')

X = df_train.drop(['Class'], axis = 1)
Y = df_train["Class"]
x_Data = X.values
y_Data = Y.values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_Data, y_Data, test_size = 0.2, random_state = 42)

"""# Naive Bayes"""

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,y_train)

model.score(X_test,y_test)

from sklearn.model_selection import cross_val_score
print(cross_val_score(GaussianNB(),X_train, y_train, cv=5))

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

pred = model.predict(X_train) 
accuracy_score(y_train, pred)

confusion_matrix(y_train, pred)

predicted_test = model.predict(X_test)
p=accuracy_score(y_test, predicted_test)

from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

print(classification_report(y_test, predicted_test))

cma = confusion_matrix(y_test, predicted_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap=plt.cm.Blues, alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Random forest Classifier"""

from sklearn.ensemble import RandomForestClassifier as rf

clf_forest = rf(n_estimators=100, max_depth=10)
clf_forest.fit(X_train, y_train)

pred = clf_forest.predict(X_train)
accuracy_score(y_train, pred)

confusion_matrix(y_train, pred)

pred_test = clf_forest.predict(X_test)
q=accuracy_score(y_test, pred_test)

from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

print(classification_report(y_test, pred_test))

cma = confusion_matrix(y_test, pred_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="coolwarm_r", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Decision Tree Classifier"""

from sklearn import tree

clf = tree.DecisionTreeClassifier()
 clf = clf.fit(X_train, y_train)

pred1 = clf.predict(X_train)
accuracy_score(y_train, pred1)

confusion_matrix(y_train, pred1)

pred1_test = clf.predict(X_test)
r=accuracy_score(y_test, pred1_test)

print(classification_report(y_test, pred1_test))

cma = confusion_matrix(y_test, pred1_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="coolwarm_r", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Logistic Regression"""

from sklearn.linear_model import LogisticRegression  
clf1= LogisticRegression(random_state=0)  
clf1.fit(X_train, y_train)

pred_LR= clf1.predict(X_train)
accuracy_score(y_train, pred_LR)

confusion_matrix(y_train, pred_LR)

pred_LR_test = clf1.predict(X_test)
s=accuracy_score(y_test, pred_LR_test)

print(classification_report(y_test, pred_LR_test))

cma = confusion_matrix(y_test, pred_LR_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="coolwarm_r", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Neural networks"""

from sklearn.neural_network import MLPClassifier

clf2= MLPClassifier(solver='lbfgs', alpha=1e-5,
           hidden_layer_sizes=(5, 2), random_state=1)
clf2.fit(X_train, y_train)

pred_NN= clf2.predict(X_train)
accuracy_score(y_train, pred_NN)

confusion_matrix(y_train, pred_NN)

pred_NN_test = clf2.predict(X_test)
u=accuracy_score(y_test, pred_NN_test)

print(classification_report(y_test, pred_NN_test))

cma = confusion_matrix(y_test, pred_NN_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="prism", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# XGBOOST"""

import xgboost as xgb

xgb = xgb.XGBClassifier()
xgb.fit(X_train,y_train)

pred_XGB= xgb.predict(X_train)
accuracy_score(y_train, pred_XGB)

confusion_matrix(y_train, pred_XGB)

pred_XGB_test = xgb.predict(X_test)
v=accuracy_score(y_test, pred_XGB_test)

print(classification_report(y_test, pred_XGB_test))

cma = confusion_matrix(y_test, pred_XGB_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="prism", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Comparative predicting"""

import numpy as np
import matplotlib.pyplot as plt
# creating the dataset
data = {'NB':p, 'RF':q, 'DT':r,'LR':s,'NN':u,'XGB':v}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 6))
# creating the bar plot
plt.bar(courses, values, color ='crimson',
		width = 0.4)
plt.xlabel("Algorithms")
plt.ylabel("Accuracy")
plt.title("Comparitive analysis of algorithm on the basis of the acccuracy")
plt.show()

activities = ['NB', 'RF', 'DT', 'LR','NN','XGB'] 
# portion covered by each label
slices = [p,q,r,s,u,v]
 
# color for each label
colors = ['red', 'blue', 'green','yellow','black','crimson']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = True, explode = (0, 0, 0.1,0,0.1,0),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()

"""# Model saving"""

filename = 'naive_bayes.sav'
joblib.dump(model, filename)
filename1 = 'random_forest_Classifier.sav'
joblib.dump(clf_forest, filename1)
filename2 = 'decision_tree_classifier.sav'
joblib.dump(clf, filename2)
filename3 = 'logistic_regression.sav'
joblib.dump(clf1, filename3)
filename4 = 'neural_networks.sav'
joblib.dump(clf2, filename4)
filename5 = 'XGBOOST.sav'
joblib.dump(xgb, filename5)
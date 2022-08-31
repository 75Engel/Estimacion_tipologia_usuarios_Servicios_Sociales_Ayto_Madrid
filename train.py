import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pickle 
from datetime import datetime
import functions as fn
import Variables as var

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,roc_auc_score,f1_score,confusion_matrix

from sklearn import metrics

var.tree_reg.fit(var.X_train, var.y_train)
y_pred = var.tree_reg.predict(var.X_test)              
print('Accuracy', accuracy_score(var.y_test, y_pred))

fn.save_files(var.tree_reg)

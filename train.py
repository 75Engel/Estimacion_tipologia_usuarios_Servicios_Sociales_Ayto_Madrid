import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pickle 
from datetime import datetime
from Utils import functions as fn
#import Variables as var                    #           Esta linea está en el fichero porque a veces me da error que no localiza el fichero Variables
from Utils import Variables as var

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,roc_auc_score,f1_score,confusion_matrix,r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics

#var.tree_reg.fit(var.X_train, var.y_train)
#fn.save_files(var.tree_reg)

#var.rnd_clf.fit(var.X_train, var.y_train)
#fn.save_files(var.rnd_clf)

var.bag_clf.fit(var.X_train, var.y_train)
fn.save_files(var.bag_clf)

#var.ada_clf.fit(var.X_train, var.y_train)
#fn.save_files(var.ada_clf)

#var.gbct.fit(var.X_train, var.y_train)
#fn.save_files(var.gbct)

#var.logreg.fit(var.X_train, var.y_train)
#fn.save_files(var.logreg)

#var.xgb_clas.fit(var.X_train, var.y_train)             #Revisar en  notebook
#fn.save_files(var.xgb_clas)

#scaler = MinMaxScaler()
#X_train_scaler=scaler.fit_transform(var.X_train)
#var.knn.fit(X_train_scaler, var.y_train)
#fn.save_files(var.knn)


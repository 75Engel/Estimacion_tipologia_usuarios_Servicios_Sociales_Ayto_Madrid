import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pickle 
from datetime import datetime
import functions as fn
import Variables as var

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,roc_auc_score,f1_score,confusion_matrix,r2_score

from sklearn import metrics

#var.tree_reg.fit(var.X_train, var.y_train)
#fn.save_files(var.tree_reg)

#var.rnd_clf.fit(var.X_train, var.y_train)
#fn.save_files(var.rnd_clf)


#var.bag_clf.fit(var.X_train, var.y_train)
#fn.save_files(var.bag_clf)

#var.ada_clf.fit(var.X_train, var.y_train)
#fn.save_files(var.ada_clf)

#var.gbct.fit(var.X_train, var.y_train)
#fn.save_files(var.gbct)

var.logreg.fit(var.X_train, var.y_train)
fn.save_files(var.logreg)

#var.xgb_clas.fit(var.X_train, var.y_train)             #Revisar en  notebook
#fn.save_files(var.xgb_clas)

#y_pred_DTR = var.tree_reg.predict(var.X_test)
#acc_DTR=accuracy_score(var.y_test, y_pred_DTR)    
#print('Accuracy', acc_DTR)

#y_pred_RFC = var.rnd_clf.predict(var.X_test)              
#acc_RFC=accuracy_score(var.y_test, y_pred_RFC)    
#print('Accuracy', acc_RFC)

#y_pred_BAG = var.bag_clf.predict(var.X_test)   
#acc_BAG=accuracy_score(var.y_test, y_pred_BAG)            
#print('Accuracy', acc_BAG)

#y_pred_ADA = var.ada_clf.predict(var.X_test)  
#acc_ADA=accuracy_score(var.y_test, y_pred_ADA)            
#print('Accuracy', acc_ADA)

#y_pred_GBCT = var.gbct.predict(var.X_test)    
#acc_GBCT=accuracy_score(var.y_test, y_pred_GBCT)
#print('Accuracy', acc_GBCT)

y_pred_LOG = var.logreg.predict(var.X_test)
acc_LOG=accuracy_score(var.y_test, y_pred_LOG)              
print('Accuracy', acc_LOG)

#y_pred_XGB = var.xgb_clas.predict(var.X_test)
#acc_XGB=accuracy_score(var.y_test, y_pred_XGB)              
#print('Accuracy', acc_XGB)



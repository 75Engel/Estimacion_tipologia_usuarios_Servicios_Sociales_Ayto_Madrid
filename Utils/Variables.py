import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression      
from sklearn.ensemble import BaggingClassifier,RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from xgboost import XGBRFClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

'''
Ficheros para modelar en DataFrames sin resample
'''

train=pd.read_csv('E:\Bootcamp_22\Javier\Repositorios\Machine_Learning\data\df_train.csv',sep=',')
test=pd.read_csv('E:\Bootcamp_22\Javier\Repositorios\Machine_Learning\data\df_test.csv',sep=',')

'''
Ficheros para modelar en DataFrames con resample
'''
#train=pd.read_csv('E:\Bootcamp_22\Javier\Repositorios\Machine_Learning\data\df_train_balanced',sep=',')
#test=pd.read_csv('E:\Bootcamp_22\Javier\Repositorios\Machine_Learning\data\df_test_balanced',sep=',')


X_test=test[['Código Distrito Centro','Age_range_code','Nationality_code','Sex_code']]
X_train=train[['Código Distrito Centro','Age_range_code','Nationality_code','Sex_code']]
y_test=test['Código Tipo Supuesto Urgente']
y_train=train['Código Tipo Supuesto Urgente']

seed= 20

estimator = DecisionTreeClassifier(max_depth=10,random_state=seed)

tree_reg = DecisionTreeClassifier(random_state=seed)

rnd_clf = RandomForestClassifier(random_state=seed)

bag_clf = BaggingClassifier(base_estimator = estimator,random_state=seed)

ada_clf = AdaBoostClassifier(base_estimator = estimator,
                             random_state=seed)

gbct = GradientBoostingClassifier(random_state=seed)

xgb_clas = XGBRFClassifier(n_estimators=100, random_state=seed)

logreg = LogisticRegression(max_iter=10000)

knn = KNeighborsClassifier(n_neighbors=5)


lista_modelos=[tree_reg,rnd_clf,bag_clf,ada_clf,gbct,logreg,knn]
lista_abr_modelos=['DTC','RND','BAG','ADA','GBCT','LOGREG','KNN']
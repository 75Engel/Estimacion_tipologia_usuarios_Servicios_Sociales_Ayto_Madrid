import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression         #   este modelo falta por añadir
from sklearn.ensemble import BaggingClassifier,RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from xgboost import XGBRFClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

train=pd.read_csv('E:\Bootcamp_22\Javier\Repositorios\Machine_Learning\data\df_train.csv',sep=',')
test=pd.read_csv('E:\Bootcamp_22\Javier\Repositorios\Machine_Learning\data\df_test.csv',sep=',')

X_test=test[['Código Distrito Centro','Age_range_code','Nationality_code','Sex_code','year']]
X_train=train[['Código Distrito Centro','Age_range_code','Nationality_code','Sex_code','year']]
y_test=test['Código Tipo Supuesto Urgente']
y_train=train['Código Tipo Supuesto Urgente']

seed= 20

tree_reg = DecisionTreeClassifier(random_state=seed)

rnd_clf = RandomForestClassifier(random_state=seed)

estimator = DecisionTreeClassifier(max_depth=10,random_state=seed)

bag_clf = BaggingClassifier(base_estimator = estimator,random_state=seed)

ada_clf = AdaBoostClassifier(base_estimator = estimator,
                             random_state=seed)

gbct = GradientBoostingClassifier(random_state=seed)

xgb_clas = XGBRFClassifier(n_estimators=100, random_state=seed)

logreg = LogisticRegression(max_iter=10000)

knn = KNeighborsClassifier(n_neighbors=5)


lista_modelos=[tree_reg,rnd_clf,bag_clf,ada_clf,gbct,logreg,knn]
lista_abr_modelos=['DTC','RND','BAG','ADA','GBCT','LOGREG','KNN']
import pickle 
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,precision_score,recall_score,roc_auc_score,f1_score,confusion_matrix
import Variables as var
import os

def save_files(model):
    '''
    Grabar modelos con formato binario en una carpeta
    '''
    date=str(datetime.today().strftime('%y%m%d%H%M%S'))
    name=input("Introduce el nombre del modelo a grabar (iniciales): ")
    path=str('Javier/Repositorios/Machine_Learning/model/')
    file=path+name+date+'.pickle'
    pickle.dump(model,open(file,'wb'))

def load_files(file,name_file):
    '''
    Cargar modelos con formato binario en un notebook o fichero python
    '''
    os.chdir('E:/Bootcamp_22/Javier/Repositorios/Machine_Learning/model')
    name_file = pickle.load( open( file, "rb" ) )

def error_modelo (model,X,y) :
    '''
    Dejamos grabada cada uno de los parámetros de cada modelo y hacemos su representación
    '''
    y_pred = model.predict(X)
    acc_model=accuracy_score(y, y_pred)
    precision_model=precision_score(y, y_pred,average='micro')
    recall_model=recall_score(y, y_pred,average='micro')
    roc_auc_model=roc_auc_score(y, model.predict_proba(X),multi_class='ovr')
    f1_model=f1_score(y, y_pred,average='micro')
    conf_model=confusion_matrix(y, y_pred, normalize='true')
    print('Accuracy', acc_model)
    print('Precision', precision_model)
    print('Recall', recall_model)
    print('ROC', roc_auc_model)
    print('F1', f1_model)

    plt.figure(figsize=(10,10))
    sns.heatmap(conf_model, annot=True);

    return f1_model,precision_model,recall_model,acc_model

def errores_modelos(lista_modelos:list): 
    '''
    Usamos una lista de los modelos entrenados para sacar sus metricas juntas y poder hacer asi una evaluación completa de todas
    '''            
    for model in var.lista_modelos:
        error_modelo(model) 

import pickle 
from datetime import datetime



def save_files(model):
    date=str(datetime.today().strftime('%y%m%d%H%M%S'))
    name=input("Introduce el nombre del modelo a grabar (iniciales): ")
    path=str('Javier/Repositorios/Machine_Learning/model/')
    file=path+name+date+'.pickle'
    pickle.dump(model,open(file,'wb'))

def load_files(file):
    model = pickle.load( open( "file", "rb" ) )



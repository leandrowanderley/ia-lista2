from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

data = pd.DataFrame([
    {'febre': 1, 'tosse': 1, 'dor_cabeca': 0, 'doenca': 'Gripe'},
    {'febre': 0, 'tosse': 1, 'dor_cabeca': 1, 'doenca': 'Resfriado'},
    {'febre': 1, 'tosse': 0, 'dor_cabeca': 1, 'doenca': 'Dengue'},
    {'febre': 1, 'tosse': 1, 'dor_cabeca': 1, 'doenca': 'COVID-19'},
    {'febre': 0, 'tosse': 0, 'dor_cabeca': 1, 'doenca': 'Enxaqueca'}
])

X = data[['febre', 'tosse', 'dor_cabeca']]
y = data['doenca']

modelo = KNeighborsClassifier(n_neighbors=1)
modelo.fit(X, y)

def diagnosticar(febre, tosse, dor_cabeca):
    sintomas = pd.DataFrame([{'febre': febre, 'tosse': tosse, 'dor_cabeca': dor_cabeca}])
    diagnostico = modelo.predict(sintomas)[0]
    return diagnostico


novo_paciente = {'febre': 1, 'tosse': 1, 'dor_cabeca': 0}
diagnostico = diagnosticar(**novo_paciente)

print(diagnostico)
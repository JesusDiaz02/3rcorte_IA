import pandas as pd
import matplotlib.pyplot as plt
from pycodestyle import tabs_obsolete

url = "caso covid"
data = pd.read_csv(url)

# Eliminar columnas del dataSet
data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

# Normalizar  Estado

data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

# Normalizar  sexo

data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'

# Normalizar  Estado

data.loc[data['Estado'] == 'M'] = 'Moderado'
data.loc[data['Sexo'] == 'F'] = 'Fallecido'

# Normalizar  Ubicacion del caso
data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'

# Normalizar  Recuperado
data.loc[data['Recuperado'] == 'fallecido'] = 'Fallecido'


#print(data.columns)


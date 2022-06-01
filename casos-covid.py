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

# Busqueda 1 número de casos de contagios en el país
#contagiosTotales = data.shape[0]
#print(f"El número de casos totales de COVID-19 son: {contagiosTotales}")

# Busqueda 2 número de municipios afectados
#NumeroMunicipiosAfectados = len(data['Nombre municipio'].value_counts())
#print(f"El número de municipios afectados es de: {NumeroMunicipiosAfectados}")

#  Busqueda 3 lista de los municipios afectados
#municipiosAfectados = set(data['Nombre municipio'])
#print(municipiosAfectados)

#  Busqueda 4 número de personas que se encuentran en atención en casa
#atencionEnCasa = len(data.loc[data['Ubicación del caso'] == 'Casa'])
#print(f"El número de personas que están siendo atendida en su casa es de: {atencionEnCasa}")


# Busqueda 5 número de personas que se encuentran recuperados
#numeroRecuperados = len(data.loc[data['Recuperado'] == 'Recuperado'])
#print(f"El número de personas que se han recuperado es de: {numeroRecuperados}")

#  Busqueda 6 número de personas que han fallecido
#numeroFallecidos = len(data.loc[data['Recuperado'] == 'Fallecido'])
#print(f"El número de personas que han fallecido es de: {numeroFallecidos}")


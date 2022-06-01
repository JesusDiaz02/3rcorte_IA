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



print(data.columns)

# Busqueda 1 número de casos de contagios en el país

#contagiosTotales = data.shape[0]
#print(f"El número de casos totales de COVID-19 son: {contagiosTotales}")

# Busqueda 2 número de municipios afectados

#NumeroMunicipiosAfectados = len(data['Nombre municipio'].value_counts())
#print(f"El número de municipios afectados es de: {NumeroMunicipiosAfectados}")

# Busqueda 3 lista de los municipios afectados

#municipiosAfectados = set(data['Nombre municipio'])
#print(municipiosAfectados)

# Busqueda 4 número de personas que se encuentran en atención en casa

#atencionEnCasa = len(data.loc[data['Ubicación del caso'] == 'Casa'])
#print(f"El número de personas que están siendo atendida en su casa es de: {atencionEnCasa}")


# Busqueda 5 número de personas que se encuentran recuperados

#numeroRecuperados = len(data.loc[data['Recuperado'] == 'Recuperado'])
#print(f"El número de personas que se han recuperado es de: {numeroRecuperados}")

# Busqueda 6 número de personas que han fallecido

#numeroFallecidos = len(data.loc[data['Recuperado'] == 'Fallecido'])
#print(f"El número de personas que han fallecido es de: {numeroFallecidos}")



# Busqueda 7 ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)

#aux = data.loc[(data['Tipo de contagio'] == 'Importado') | (data['Tipo de contagio'] == 'Relacionado') | (data['Tipo de contagio'] == 'En estudio')]
#tipoCasoContagio = aux['Tipo de contagio'].value_counts()
#print(tipoCasoContagio)


# Busqueda 8  número de departamentos afectados

#numeroDepartamentosAfectados = len(data['Nombre departamento'].value_counts())
#print(f"El número de departamentos afectados es de {numeroDepartamentosAfectados}")

# Busqueda 9 lista de departamentos afectados

#depatamentossAfectados = set(data['Nombre departamento'])
#print(depatamentossAfectados)

# Busqueda 10 Ordenar de mayor a menor por tipo de recuperación (Tipo de atención esta)

#ordenarTipoAtencion = data['Tipo de recuperación'].value_counts()
#print(ordenarTipoAtencion)


# Busqueda 11 listar de mayor a menor los 10 departamentos con más casos de contagios

#top10 = data['Nombre departamento'].value_counts().head(10)
#print(top10)

# Busqueda 12 listar de mayor a menor los 10 departamentos con más fallecidos

#aux = data.loc[data['Recuperado'] == 'Fallecido']
#top10D-2 = aux['Nombre departamento'].value_counts().head(10)
#print(top10-2)


# Busqueda 13 listar de mayor a menor los 10 departamentos con más recuperados

#aux = data.loc[data['Recuperado'] == 'Recuperado']
#top10-3 = aux['Nombre departamento'].value_counts().head(10)
#print(top10-3)

# Busqueda 14 listar de mayor a menor los 10 municipios con más casos de contagios

#top10-4 = data['Nombre de municipio'].value_counts().head(10)
#print(top10-4)


# Busqeuda 15 liste de mayor a menor los 10 municipios con mas casos de
# fallecidos

# aux = data.loc[data['Recuperado'] == 'Fallecido']
# municipiosConMasMuertos = aux['Nombre municipio'].value_counts().head(10)
# print(municipiosConMasMuertos)


# busqueda 16 liste de mayor a menor los 10 municipios con mas casos de
#recuperados

#aux = data.loc[data['Recuperado'] == 'Recuperado']
#municipiosConMasRecuperados = aux['Nombre municipio'].value_counts().head(10)
#print(municipiosConMasRecuperados)


# busqueda 17 liste agrupado por departamento y en orden de Mayor a menor las
#ciudades con mas casos de contagiados

#top10-5 = data.groupby(['Nombre departamento'])
#print(top10-5['Nombre municipio'].value_counts())

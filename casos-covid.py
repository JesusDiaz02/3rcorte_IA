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


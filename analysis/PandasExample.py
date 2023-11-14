import pandas as pd

#Fuente de datos
ciudades = ['jerusalen', 'telavit', 'kiev', 'itagui', 'pitalito']
#Convertir una lista en dataframe
dataframeCiudades = pd.DataFrame({'Ciudad': ciudades})
#print (dataframeCiudades)

#lista diccionarios coleccion

estudiantes = [
    {'id': 1, 'nombre': 'Juan Dicotecas', 'promedio': 0.0},
    {'id': 2, 'nombre': 'Santi el bicho', 'promedio': 2.5},
    {'id': 3, 'nombre': 'santi diomedez', 'promedio': 2.0},
    {'id': 4, 'nombre': 'susana', 'promedio': 1.8},
    {'id': 5, 'nombre': 'Juancho Styles', 'promedio': 0.0}

]
#convertir los datos de entrada en un dataframe

dataFrameEstudiantes = pd.DataFrame(estudiantes)
#print (dataFrameEstudiantes)
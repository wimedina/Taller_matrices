# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 08:36:34 2021

@author: William Medina
"""
import numpy as np
import pandas as pd

data = 'Casos_positivos_de_COVID-19_en_Colombia.csv'

df = pd.read_csv(data)

# 1. Número de casos de Contagiados en el País.

df.shape[0]

# 2. Número de Municipios Afectados

df.groupby('Nombre municipio').size().shape[0]

# 4. Número de personas que se encuentran en atención en casa

# Unificar los datos para ubicación Casa


df.loc[df['Ubicación del caso'] == 
       'CASA', 'Ubicación del caso'] = 'Casa'
       
df.loc[df['Ubicación del caso'] == 
       'casa', 'Ubicación del caso'] = 'Casa'

#Contar el numero de personas

df[df['Ubicación del caso']== 'Casa'].shape[0]

#6. Número de personas que ha fallecido

df[df['Estado'] == 'Fallecido'].shape[0]


# 8. Número de departamentos afectados

df['Nombre departamento'].value_counts().shape[0]
 
 #9. Liste los departamentos afectados(sin repetirlos)
 
 df['Nombre departamento'].value_counts()
 
 # 11.Liste de mayor a menor los 10 departamentos con mas casos de contagiados
 
df['Nombre departamento'].value_counts().head(10)


# 12 Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

df[df['Estado'] =='Fallecido']['Nombre departamento'].value_counts().head(10)

# 13.Liste de mayor a menor los 10 departamentos con mas casos de recuperados

df[df['Recuperado'] =='Recuperado']['Nombre departamento'].value_counts().head(10)


# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados

df['Nombre municipio'].value_counts().head(10)

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos

df[df['Estado'] =='Fallecido']['Nombre municipio'].value_counts().head(10)

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados

df[df['Recuperado'] =='Recuperado']['Nombre municipio'].value_counts().head(10)

# 20. Liste de mayor a menor el número de contagiados por país de procedencia
 
 df['Nombre del país'].value_counts().sort_values(ascending = False)
 
 # 21. Liste de mayor a menor las fechas donde se presentaron mas contagios

df['Fecha de notificación'].value_counts().sort_values(ascending = False)


# 30. Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia.

df[df['Estado'] =='Fallecido'][df['Unidad de medida de edad'] == 
                               1]['Edad'].value_counts().sort_values(ascending = False)

 
 

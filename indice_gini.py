import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Cargar el archivo CSV
archivo_csv = "C:\\Users\\vanev\\OneDrive\\Proyecto final\\P_Data_Extract_From_World_Development_Indicators\\869566ef-4e59-46bf-953e-a7241a12b16c_Data.csv"
datos = pd.read_csv(archivo_csv)

# Mostrar las primeras filas de los datos para verificar que se hayan cargado correctamente
print(datos.head())

# Lista de países de América Latina
paises_latinoamerica = [
    "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Costa Rica", "Cuba",
    "República Dominicana", "Ecuador", "El Salvador", "Guatemala", "Haití", "Honduras",
    "México", "Nicaragua", "Panamá", "Paraguay", "Perú", "Puerto Rico", "Uruguay", "Venezuela"
]

# Filtrar los datos para incluir solo los países de América Latina
datos_latinoamerica = datos[datos["Country Name"].isin(paises_latinoamerica)]

# Mostrar las primeras filas de los datos filtrados
print(datos_latinoamerica.head())

# ---------------------- Cálculo del índice de Gini ----------------------

# Configurar el tamaño del gráfico
'''plt.figure(figsize=(10, 6))

# Iterar sobre cada país de América Latina y trazar su Índice de Gini a lo largo del tiempo
for pais in paises_latinoamerica:
    datos_pais = datos_latinoamerica[datos_latinoamerica["Country Name"] == pais]
    if not datos_pais.empty:  # Verificar si datos_pais no está vacío
        anios = datos_pais.columns[4:]  # Columnas correspondientes a los años
        valores_gini = datos_pais.iloc[0, 4:].replace('..', np.nan).astype(float)  # Reemplazar '..' con NaN y convertir a float
        plt.plot(anios, valores_gini, label=pais)

# Configurar etiquetas y leyenda
plt.xlabel('Año')
plt.ylabel('Índice de Gini')
plt.title('Evolución del Índice de Gini en países de América Latina')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mejorar la legibilidad
plt.tight_layout()
plt.show()'''

print('---------------------- Cálculo del índice de Gini ----------------------')

# Seleccionar solo las columnas comunes entre el Índice de Gini y el PIB per cápita
columnas_comunes = datos_latinoamerica.columns.intersection(['Country Name', '2010 [YR2010]', '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]', '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]', '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]'])
datos_comunes = datos_latinoamerica[columnas_comunes]

print(datos_comunes.columns)

# Seleccionar los datos relevantes para el modelo de regresión lineal
X = datos_comunes[['2014 [YR2014]', '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]', '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]']].replace('..', np.nan).astype(float)
y = datos_comunes['Gini index'].astype(float)

# # Inicializar el modelo de regresión lineal
modelo = LinearRegression()

# # Ajustar el modelo a los datos
modelo.fit(X, y)

# # Imprimir los coeficientes de la regresión
#print("Coeficiente de la regresión:", modelo.coef_)
#print("Intercepto de la regresión:", modelo.intercept_)

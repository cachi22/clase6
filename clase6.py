# import pandas as pd

# edades_serie = pd.Series([22,14,35,19,5,27,56])
# print(edades_serie)
# #print(edades[5])

# cadenas_numeros = pd.Series(["perro",4, "gato", 4, "pajaro", 2])
# print(cadenas_numeros)

# indices = cadenas_numeros.index
# print(indices)

# cant_elem = cadenas_numeros.count()
# print("Cuantos elementos hay en la serie? ", cant_elem)

# suma_edades = edades_serie.sum()
# max_edades = edades_serie.max()
# min_edades = edades_serie.min()
# prom_edades = edades_serie.mean()
# print(f'la suma de las edades es {suma_edades}')
# print(f'el maximo de las edades es {max_edades}')
# print(f'el minimo de las edades es {min_edades}')
# print(f'la promedio de las edades es {prom_edades}')
# #print(edades_serie.describe())

# nombre_alturas = pd.DataFrame([
#                                 ["martina", 1.50],
#                                 ["juan",    1.80],
#                                 ["ana",     1.60],
#                                 ["luis",    1.70]
# ])
# print(nombre_alturas)

# print(nombre_alturas.index)
# print(nombre_alturas.describe())
# print(nombre_alturas.columns)
# print(nombre_alturas[0])
# print(nombre_alturas[1])
# alturas = nombre_alturas[1]
# print(alturas)
# print(nombre_alturas.loc[0])
# print(nombre_alturas.iloc[1:])

# df_nuevo = nombre_alturas.loc[1:]
# print(df_nuevo)

# print(df_nuevo.loc[1])
# print(df_nuevo.iloc[1])

# nombre_alturas.columns = ["nombres", "alturas"]
# print(nombre_alturas)

# nombre_alturas["edades"]= [22,12,4,26]
# print(nombre_alturas)

# materia_horas = {'materias': ['biologia','matematica','historia', 'quimica'],
#                 'horas_semanales' :[6,4,8,8]}

# df_mater_hor = pd.DataFrame(materia_horas)
# print(df_mater_hor)

# def duplicar(valor):
#     return valor*2

# df_mater_hor['horas_duplicadas'] = df_mater_hor['horas_semanales'].apply(duplicar)
# print(df_mater_hor)

# def calcular_promedio( dataFrame, nombre_columna):
#     columna = dataframe [nombre_columna]
#     promedio = columna.mean()
#     return 

import pandas as pd

def calcular_promedio(data_frame, nombre_columna):
    if nombre_columna in data_frame.columns:
        promedio = data_frame[nombre_columna].mean()
        return promedio
    else:
        return f"La columna '{nombre_columna}' no existe en el DataFrame."

# Ejemplo de uso:
data = {'Nombre': ['Juan', 'Ana', 'Pedro', 'Luis'],
        'Edad': [25, 30, 28, 22]}

df = pd.DataFrame(data)

columna_a_promediar = 'Edad'
resultado = calcular_promedio(df, columna_a_promediar)
if isinstance(resultado, str):
    print(resultado)
else:
    print(f"El promedio de la columna '{columna_a_promediar}' es: {resultado}")


def contar_repeticiones(data_frame):
    conteo = {}
    for columna in data_frame.columns:
        valores_unicos = data_frame[columna].unique()
        for valor in valores_unicos:
            conteo[valor] = data_frame[columna].value_counts()[valor]
    return conteo

# Ejemplo de uso:
data = {'Color': ['Rojo', 'Verde', 'Azul', 'Rojo', 'Azul', 'Verde', 'Rojo']}
df = pd.DataFrame(data)

resultado = contar_repeticiones(df)
print(resultado)


def convertir_a_minusculas(data_frame):
    df_copy = data_frame.copy()

    for columna in df_copy.columns:
        if df_copy[columna].dtype == 'object':
            df_copy[columna] = df_copy[columna].str.lower()
    
    return df_copy

# Ejemplo de uso:
data = {'Nombre': ['Juan', 'Ana', 'Pedro', 'Luis'],
        'Apellido': ['Gomez', 'Perez', 'Lopez', 'Martinez']}

df = pd.DataFrame(data)

df_en_minusculas = convertir_a_minusculas(df)

print(df_en_minusculas)

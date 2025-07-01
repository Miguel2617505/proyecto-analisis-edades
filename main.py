import pandas as pd

datos= {
    "Nombre": ["Miguel", "Laura", "Jarvis", "Jimmy", "Nidia"],
    "Edad": [24, 20, 24, 51, 52],
    "Ciudad": ["Bogotá", "Bogotá", "Cyberespacio", "Medellín", "Santander"],
    "Sexo": ["Hombre", "Mujer", "Hombre", "Hombre", "Mujer"],
    "Estado Civil": ["Casado", "Casado", "Soltero", "Casado", "Casado"]
}
#llamamos al pd y creamos la tabla de datos (DataFrame)
df= pd.DataFrame(datos)

print("\nTabla para impresionar a Jarvis")
print(df)

#Paso 2 filtrar de menor a mayor
df_ordenado = df.sort_values(by="Edad")
print(df_ordenado)

#Agregar las edades que se tendrán en 5 años

df["Edad en 5 años"] = df["Edad"] + 5
print(df)

#Ahora haremos el promedio de datos real

promedio = df["Edad"].mean()

print(f"\nPromedio de edad: {promedio: .1f} años")

#Imprimirla cmo archivo .csv

df.to_csv("analisis_edades.csv", index=False)
print("\nArchivo guardado como analisis_edades.csv")
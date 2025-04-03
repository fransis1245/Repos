import os
import requests

# 1. Definimos las categorías de imágenes que queremos
categorias = ["categoria A", "categoria B", "categoria C"]

# 2. Creamos una carpeta para cada categoría
for categoria in categorias:
    os.makedirs(categoria, exist_ok=True)  # 'exist_ok=True' evita errores si la carpeta ya existe

# 3. Descargamos 3 imágenes para cada categoría
for categoria in categorias:
    for i in range(3):  # Descargaremos 3 imágenes por categoría
        # Usamos la API de Lorem Picsum (imágenes aleatorias)
        url = "https://picsum.photos/200"  # 200x200 píxeles
        
        # Hacemos la petición a internet
        respuesta = requests.get(url)
        
        # Si la petición fue exitosa (código 200)
        if respuesta.status_code == 200:
            # Guardamos la imagen en la carpeta correspondiente
            nombre_archivo = f"{categoria}/imagen_{i+1}.jpg"
            with open(nombre_archivo, "wb") as archivo:  # 'wb' = escribir en modo binario
                archivo.write(respuesta.content)
            print(f"Imagen guardada: {nombre_archivo}")
        else:
            print(f"Error al descargar imagen {i+1} de {categoria}")
            
print("¡Todas las imágenes se han descargado!")
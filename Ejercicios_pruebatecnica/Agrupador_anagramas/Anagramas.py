def agrupar_anagramas():
    # Creamos la lista (arreglo en Java)
    nombres = ["eat", "tea", "tan", "ate", "nat", "bat"]
   
    # Creamos un diccionario para guardar los grupos
    # En Python, un dict funciona como el HashMap de Java
    grupos = {}

    # Recorremos los nombres
    for palabra in nombres:
        # Convertimos la palabra en una lista de caracteres, la ordenamos
        # y la volvemos a unir para crear la "llave"
        clave = "".join(sorted(palabra))
       
        # Si la clave no está en el diccionario, inicializamos una lista vacía
        if clave not in grupos:
            grupos[clave] = []
       
        # Agregamos la palabra original al grupo correspondiente
        grupos[clave].append(palabra)

    # Validamos imprimiendo los resultados
    for grupo in grupos.values():
        print(grupo)

# Ejecutar la función
if __name__ == "__main__":
    agrupar_anagramas()
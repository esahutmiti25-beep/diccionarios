
# 10 EJERCICIOS DE INDEXACION Y BUSQUEDA RAPIDA

# EJERCICIO 1: Diccionario de estudiantes
print("\n--- EJERCICIO 1: ESTUDIANTES ---")

estudiantes = {
    "Ana": 9,
    "Luis": 8,
    "Carlos": 10
}

print("Calificacion de Ana:", estudiantes["Ana"])


# EJERCICIO 2: Buscar productos por codigo
print("\n--- EJERCICIO 2: PRODUCTOS ---")

productos = {
    101: "Teclado",
    102: "Mouse",
    103: "Monitor"
}

print("Producto con codigo 102:", productos[102])


# EJERCICIO 3: Buscar una palabra
print("\n--- EJERCICIO 3: DICCIONARIO DE PALABRAS ---")

definiciones = {
    "computadora": "Dispositivo electronico",
    "internet": "Red mundial",
    "programacion": "Creacion de software"
}

print("Definicion:", definiciones.get("computadora", "No encontrada"))


# EJERCICIO 4: Contar frecuencia de palabras
print("\n--- EJERCICIO 4: FRECUENCIA DE PALABRAS ---")

texto = "hola mundo hola python mundo hola"
frecuencia = {}

for palabra in texto.split():
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia:", frecuencia)


# EJERCICIO 5: Actualizar informacion
print("\n--- EJERCICIO 5: EMPLEADOS ---")

empleados = {
    "Pedro": 8000,
    "Maria": 9000,
    "Jose": 7500
}

empleados["Maria"] = 10000

print("Empleados actualizados:", empleados)


# EJERCICIO 6: Buscar numeros telefonicos
print("\n--- EJERCICIO 6: AGENDA TELEFONICA ---")

agenda = {
    "Juan": "4421234567",
    "Sofia": "4429876543",
    "Miguel": "4424567890"
}

nombre = "Sofia"

print("Telefono:", agenda.get(nombre, "Contacto no encontrado"))


# EJERCICIO 7: Buscar alumnos por matricula
print("\n--- EJERCICIO 7: MATRICULAS ---")

alumnos = {
    "A001": "Daniel",
    "A002": "Fernanda",
    "A003": "Roberto",
    "A004": "Andrea"
}

matricula = "A003"

print("Alumno:", alumnos.get(matricula, "Alumno no encontrado"))


# EJERCICIO 8: Comprobar claves existentes
print("\n--- EJERCICIO 8: INVENTARIO ---")

inventario = {
    "P01": "Laptop",
    "P02": "Celular",
    "P03": "Tablet"
}

codigo = "P02"

if codigo in inventario:
    print("Producto encontrado:", inventario[codigo])
else:
    print("Producto no encontrado")


# EJERCICIO 9: Resolver colisiones mediante encadenamiento
print("\n--- EJERCICIO 9: COLISIONES HASH ---")

tabla = {}

def insertar(clave, valor):
    indice = clave % 5

    if indice not in tabla:
        tabla[indice] = []

    tabla[indice].append((clave, valor))

insertar(10, "Ana")
insertar(15, "Luis")
insertar(20, "Carlos")

print("Tabla hash:", tabla)


# EJERCICIO 10: Busqueda mediante funcion Hash
print("\n--- EJERCICIO 10: BUSQUEDA HASH ---")

def hash_func(clave):
    return clave % 10

productos_hash = {
    hash_func(101): "Teclado",
    hash_func(102): "Mouse",
    hash_func(103): "Monitor"
}

codigo = 102
indice = hash_func(codigo)

print("Producto encontrado:", productos_hash[indice])


# FIN DEL PROGRAMA
print("\n--- LOS 10 EJERCICIOS HAN TERMINADO ---")

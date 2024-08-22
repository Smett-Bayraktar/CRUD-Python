lista = ["Oscar"]

def crearUsuario (array): #Create
    name = input("Ingrese el nombre del usuario: ").capitalize() #Creamos una variable que guardara un nombre, y siempre sera con la primera letra en Mayuscula
    while name in array: #Mientras el dato de la variable "name" este dentro del array, se ejecutara el siguiente codigo que en pocas palabras verifica si el dato se repite en la lista o no
        print("Escoga otro nombre")
        name = input("Ingrese el nombre del usuario: ")
    array.append(name.capitalize()) #Agrega el dato de la variable "name" dentro de la lista "array" siempre con la primera letra en Mayuscula
    print("-"*10)
    print(f"El nombre {name.capitalize()} fue agregado con exito")

def mostrarDatos(array): #Read
    for i in array:
        print(f"Nombre: {i}")
        print("-"*10)

def modificarUsuario(array): #Update
    name = input("Ingrese el nombre que quiere modificar: ")
    if name.capitalize() in array:
        print("-"*10)
        newName = input(f"modifique el nombre {name.capitalize()}: ").capitalize()
        if newName in array:
            print("-"*10)
            print(f"el nombre {newName} ya existe")
        else:
            array.remove(name.capitalize())
            array.append(newName)
            print("-"*10)
            print(f"El nombre {name.capitalize()} fue modificado por: {newName.capitalize()}")
        
def eliminarUsuario(array): #Delete
    name = input("Ingrese el nombre de usuario que quiere eliminar: ")
    if name.capitalize() in array:
        print("-"*10)
        print(f"El nombre: {name.capitalize()} fue removido")
        array.remove(name.capitalize())

print("Bienvenido, eliga las siguientes opciones para el menu")
while True:
    print("1.Insertar Usuario \n2.Mostrar Usuarios\n3.Modificar Usuario\n4.Eliminar Usuario\n5.Salir")
    opcion = int(input("Elija: "))
    if opcion == 1:
        crearUsuario(lista)
        print("-"*10)
    elif opcion == 2:
        print("-"*10)
        mostrarDatos(lista)
    elif opcion == 3:
        modificarUsuario(lista)
        print("-"*10)
    elif opcion == 4:
        eliminarUsuario(lista)
        print("-"*10)
    elif opcion == 5:
        print("Hasta Luego!!")
        break


"""
CONSIGNAS
Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.

Formato
El proyecto debe compartirse utilizando Colab bajo el nombre “Primera pre-entrega+Apellido”.

Sugerencias:
El formato de registro es: Nombre de usuario y Contraseña.
Utilizar una función para almacenar la información y otra función para mostrar la información.
Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
"""

"""
Resumen del trabajo
En esta oportunidad voy a crear este proyecto como un sitio web similar a Pinterest donde los usuarios pueden subir fotos (almcacenarlas), y ver tambien las fotos de otros usuarios.
"""

#Importo las librerias de JSON y OS
import json
import os

#Diccionario para almacenar la informacion de los users & pass
database = {}

def createDB():
    if not os.path.exists("database.json"):
        with open("database.json", "w") as file:
            json.dump({"name": "users", "users": {}}, file)

#Creacion de base de datos
createDB()

#Aca defino la funcion de registro de nuevos usuarios
def register():
    email = input("Ingrese su email: ")
    name = input("Ingrese su nombre: ")
    lastName = input("Ingrese su apellido: ")
    password = input("Cree una contrasenia: ")

    if email in database: #Me fijo si el mail ya esta guardado, if True:
        print("Atencion! Ese email ya esta registrado.")
    else:
        database[email] = {
            "Nombre": name,
            "Apellido": lastName,
            "Contrasenia": password
        }
        with open("database.json", "w") as file: #Aca almaceno el nuevo user en el JSON
            json.dump(database, file)
        print("Bienvenido! Se ha registrado correctamente.")

#Aca defino la funcion de logueo de usuarios ya existentes
def login():
    email = input("Ingrese su email: ")
    password = input("Ingrese su contrasenia: ")

    with open("database.json", "r") as file:
        database = json.load(file)

    if email in database and database[email]["Contrasenia"] == password: #Aca verifico dos cosas: 1) que el email este almacenado en la base de datos; y 2) que el email y la contrasenia coincidan
        print("Ha ingresado a su cuenta de Pinterest.") #Yay!
    else:
        print("Email o contrasenia invalidos.") #Si algo de lo anterior es False, entonces se ejecuta este print.

#Aca defino la funcion de lectura de la database
def readInfo():
    import json
    email = input("Ingrese su email: ")
    if email in database: #Si el mail esta almacenado en la database (if True):
        with open("database.json", "r") as file:
            for line in file:
                data = json.loads(line)
                if email in data:
                    info = data[email]
                    print(f"Esta es la informacion almacenada sobre {email}: {info}")
    else:
        print("El email ingresado no es valido.")

#Aca configuro la ejecucion de todas las funciones que defini anteriormente
while True:
    print("--- OPCIONES ---")
    print("1. Registrarse")
    print("2. Ingresar a su cuenta")
    print("3. Ver informacion almacenada")
    print("4. Salir")

    choice = input("Elija una de las opciones anteriores (ingrese solo el numero): ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        readInfo()
    elif choice == "4":
        break        
    else:
        print("Ha ingresado una opcion invalida. Recuerde que debe ingresar un numero del 1 al 4.")

"""
Notas:
No puse como opcion 1 "crear una base de datos" porque en la realidad ningun programa/website te permite crear una base de datos sino que ya esta creada, o en este caso, se crea con el registro del primer usuario. Los usuarios que se creen a continuacion se almacenaran en esa misma base de datos.
"""
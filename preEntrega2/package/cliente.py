from .carrito import Carrito
from .producto import Producto

class Cliente:
    def __init__(self, name, lastName, age, email, address):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.email = email
        self.address = address
        self.carrito = Carrito()

    def __str__(self):
        return f"Client: {self.name} {self.lastName}"
        #Probar un print aca

    def purchase(self, producto):
        self.carrito.addProduct(producto)
        print(f"{self.name} {self.lastName} ha comprado el producto {producto}.")

    def updateAddress(self, newAddress):
        self.address = newAddress
        print(f"{self.name} {self.lastName} ha actualizado su direccion a {self.address}")

    def paymentMethod(self, paymentMethod):
        print(f"{self.name} {self.lastName} ha elegido {paymentMethod} como metodo de pago.")


"""
#Ejemplo de uso
client1 = Client("Barney", "Stinson", 29, "male", "barney@gmail.com", "Calle Falsa 123")
print(client1)
#Imprime: Client: Barney Stinson (solo eso!!!)

client1.purchase(input("Que desea comprar?:"))
#Aca primero te pregunta que queres comprar, lo completas en la terminal y ahi te imprime "Barney Stinson has purchased LO QUE SEA QUE HAYAS COMPLETADO"
#Probado y funciona ok

client1.sell(input("Que desea vender?:"))

client1.updateAddress(input("Cual es tu direccion?:"))

client1.paymentMethod(input("Como te gustaria abonar?:"))
"""
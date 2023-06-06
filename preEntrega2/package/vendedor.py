from .carrito import Carrito
from .producto import Producto

class Vendedor:
    def __init__(self, name, lastName, age, email, address):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.email = email
        self.address = address

    def __str__(self):
        return f"Vendedor: {self.name} {self.lastName}"

    def sell(self, product):
        #No configuro toda la logica de la venta del producto porque no me funciono, lo tengo en un archivo a parte. Solo dejo el print de la venta. No elimina el producto del JSON ni vacia el Carrito.
        print(f"Se ha vendido el producto {product}")

    def chargeMethod(self, method):
        #Igual que en el metodo anterior, pretendo configurar que el metodo de pago aceptado por el Vendedor sean las unicas opciones dadas para el metodo de pago indicado por el Comprador. Todavia no llegue a eso.
        print(f"El Vendedor solamente acepta como metodo de pago: {method}")
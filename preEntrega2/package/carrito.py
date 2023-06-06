import json
from package.producto import Producto

class Carrito:
    def __init__(self):
        self.productos = []

    def addProduct(self, producto):
        self.productos.append(producto)
        print(f"Se ha agregado {producto} al carrito.")

    def removeProduct(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Se ha eliminado {producto} del carrito.")
        else:
            print(f"{producto} no se encuentra en el carrito.")

    def emptyCarrito(self):
        self.productos = []
        print("El carrito se ha vaciado.")

    def showProducts(self):
        if self.productos:
            print("Estos son los productos en el carrito:")
            for producto in self.productos:
                print(f"-{producto}")
        else:
            print("El carrito está vacío.")
    
    def saveCarrito(self, carritoJSON):
        with open(carritoJSON, 'w') as file:
            json.dump(self.productos, file)
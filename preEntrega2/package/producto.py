import json

class Producto:
    def __init__(self, productName, description, price):
        self.productName = productName
        self.description = description
        self.price = price

    def addToCart(self, carrito):
        carrito.addProduct(self)

    def removeFromCart(self, carrito):
        carrito.removeProduct(self)

    def emptyCart(self, carrito):
        carrito.emptyCarrito()

    def showCart(self, carrito):
        carrito.showProducts()

    def saveToJson(self, productJSON):
        with open(productJSON, 'w') as file:
            json.dump(self.__dict__, file)

    def __str__(self):
        return f"{self.productName} a ${self.price}"
"""
La Clase Clientes deberia funcionar optima. Estoy tratando de emular un e-commerce que hice en un curso de Desarrollo Web con JavaScript y NodeJS, pero creo que me la complique demasiado sola para la segunda entrega.

Lo minimo para esta entrega esta funcional. El codigo comentado lo dejo por si te interesa revisarlo y por si tenes alguna sugerencia para agregar.
"""
from package.cliente import Cliente
from package.carrito import Carrito
from package.producto import Producto
from package.vendedor import Vendedor

#Creo instancia de Cliente
#name, lastName, age, email, address
print("---Creo una instancia de Cliente---")
cliente = Cliente("Tony", "Stark", 30, "tonystark@gmail.com", "Calle Falsa 123")
print(cliente)

#Creo instancia de Vendedor
#name, lastName, age, email, address
print("---Creo una instancia de Vendedor---")
vendedor = Vendedor("Natasha", "Romanoff", 28, "natasha@gmail.com", "Boulevard 456")
print(vendedor)

#Creo instancias de productos
#productName, description, price
producto1 = Producto("Moto", "Excelente moto para salvar al mundo de alienigenas", 10000)
producto2 = Producto("Traje de combate", "Traje de combate super flexible para pelear contra villanos", 58.99)

#Creo un carrito
carrito = Carrito()

#Agrego los productos al carrito
print("---Agrego productos creados al carrito con el metodo addToCart---")
producto1.addToCart(carrito)
producto2.addToCart(carrito)

#Muestro los productos del carrito
print("---Uso el metodo showProducts y muestro un listado de productos del Carrito---")
carrito.showProducts()

"""#Nuestro Cliente Tony Stark hace una compra
print("---Uso el metodo purchase y muestro lo que compro mi Cliente---")
cliente.purchase(carrito)"""

#Nuestro Cliente Tony Stark actualiza su direccion
print("---Uso el metodo updateAddress y muestro la nueva direccion de mi Cliente---")
cliente.updateAddress("890 5th Av., Manhattan, Nueva York")  # Es el edificio de los Avengers jaja

#Aca hago que el Cliente Tony Stark elija su metodo de pago preferido.
print("---Uso el metodo paymentMethod y muestro el metodo de pago elegido por mi Cliente---")
cliente.paymentMethod("Tarjeta de crédito")

#-------------------CODIGO COMENTADO QUE QUIERO GUARDAR PARA FUTURO---------------------------------
#No logro sacar la logica para que el Vendedor pueda efectivamente vender un producto (y que se elimine del JSON). Quiero arreglar bien el JSON de Producto primero.

#Nuestra Vendedora Natasha Romanoff hace una venta
#vendedor.sell(producto1)

#Aca hago que la Vendedora Natasha Romanoff elija su forma de cobro preferida. Igual esto lo comento porque comente toda la Clase Vendedor. No me andaba bien, quiero arreglarla.
#vendedor.chargeMethod("Transferencia bancaria")
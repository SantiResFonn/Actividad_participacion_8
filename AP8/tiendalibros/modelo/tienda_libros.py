class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self, carrito) -> None:
            self.catalogo = {isbn:carrito.CarroCompras}
    def __str__(self) -> str:
        representacion = "El libro con titulo {}".format(self.catalogo), "{} y isbn:" .format(self.isbn), "ya existe en el catalogo"
    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):
        if catalogo.contains(isbn):
            LibroExistenteError
        else:
            libro_nuevo = Libro(isbn,titulo,precio,existencias)
            return catalogo.append(libro_nuevo)
        while True:
            try:
                LibroAgotadoError
            except LibroError

    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro, unidades):
        
    # Defina metodo retirar_item_de_carrito
    def retirar_item_carrito(self, isbn)
        return carrito.quitar_item()
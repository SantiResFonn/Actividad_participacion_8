import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras
    def retirar_libro_de_Carrito_compras(self):
        isbn = input("Ingrese el isbn del libro que va a retirar: ")
        self.retirar_item_de_Carrito(isbn)
        print("El libro se ha retirado del catalogo")
    # Defina el metodo agregar_libro_a_carrito_de_compras
    def agregar_libro_a_carrtio_de_compras(self, isbn:str, cantidad: int)
        
    # Defina el metodo adicionar_un_libro_a_catalogo
    def adicionar_un_libro_a_catalogo(self, isbn: str, titulo: str,precio: float,existencias: int):

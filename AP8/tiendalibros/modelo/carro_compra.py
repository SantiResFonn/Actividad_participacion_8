class CarroCompras:
    def __init__(self) -> None:
        self.item: list = []
    # Defina el metodo agregar_item
    def agregar_item(self,libro,cantidad):
        item = ItemCompra(libro,cantidad)
        return self.item.append(item)
    # Defina el metodo calcular_total
    def calcular_total(self):
        total = 0
        for i in self.item.calcular_total():
            total+=i
    # Defina el metodo quitar_item
    def quitar_item(self,isbn):
        self.item = [self.item.remove(isbn) for isbn in self.item if self.item.contains(isbn)]
    
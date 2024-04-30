class ItemCompra:
    def __init__(self, libro, cantidad: int) -> None:
        self.libro = libro
        self.cantidad = cantidad
    def calcular_subtotal(self,cantidad,precio):
        return cantidad*precio
    

        

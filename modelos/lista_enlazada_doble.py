from .nodo import Nodo

class ListaEnlazadaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._tam = 0

    def esta_vacia(self):
        return self.primero is None

    def __len__(self):
        return self._tam

    def contar(self):
        return self._tam

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
        self._tam += 1

    def iterar(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato   
            actual = actual.siguiente

    def buscar_por_id(self, id_buscar):
        actual = self.primero
        while actual is not None:
            cliente = actual.dato
            if getattr(cliente, "id", None) == id_buscar:
                return cliente
            actual = actual.siguiente
        return None

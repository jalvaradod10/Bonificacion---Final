from modelos.lista_enlazada_doble import ListaEnlazadaDoble
from modelos.cliente import Cliente

class Sistema:
    def __init__(self):
        self.clientes = ListaEnlazadaDoble()
        self._siguiente_id = 1
        self._sembrar_clientes_iniciales()

    def registrar_cliente(self, nombre, apellido, telefono):
        nuevo = Cliente(self._siguiente_id, nombre, apellido, telefono)
        self.clientes.agregar_al_final(nuevo)
        self._siguiente_id += 1
        return nuevo

    def iterar_clientes(self):
        return self.clientes.iterar()

    def cantidad_clientes(self):
        return self.clientes.contar()

    def eliminar_logico_cliente(self, id_cliente):
        cliente = self.clientes.buscar_por_id(id_cliente)
        if cliente is None:
            return False, "No existe un cliente con ese ID."
        if not cliente.activo:
            return False, "Ese cliente ya está inactivo."
        cliente.activo = False
        return True, "Cliente marcado como inactivo correctamente."

    def _sembrar_clientes_iniciales(self):
        self.registrar_cliente("Ana", "Pérez", "3001234567")
        self.registrar_cliente("Luis", "Gómez", "3017654321")
        self.registrar_cliente("María", "Rojas", "3025556677")
        self.registrar_cliente("Carlos", "Torres", "3031112233")
        self.registrar_cliente("Daniela", "Martínez", "3044445566")

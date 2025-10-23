# servicios/sistema.py
# Lógica del sistema: gestiona la lista de clientes (lista doble),
# registro, listado y baja lógica.
# Incluye una "siembra" (clientes iniciales ya cargados).

from modelos.lista_enlazada_doble import ListaEnlazadaDoble
from modelos.cliente import Cliente

class Sistema:
    def __init__(self):
        self.clientes = ListaEnlazadaDoble()
        self._siguiente_id = 1  # ID autoincremental sencillo
        self._sembrar_clientes_iniciales()

    # --- Registrar cliente ---
    def registrar_cliente(self, nombre, apellido, telefono):
        nuevo = Cliente(self._siguiente_id, nombre, apellido, telefono)
        self.clientes.agregar_al_final(nuevo)
        self._siguiente_id += 1
        return nuevo

    # --- Listar clientes (activos e inactivos para ver estado) ---
    def listar_clientes(self):
        return list(self.clientes.iterar())

    # --- Eliminación lógica por ID ---
    def eliminar_logico_cliente(self, id_cliente):
        cliente = self.clientes.buscar_por_id(id_cliente)
        if cliente is None:
            return False, "No existe un cliente con ese ID."
        if not cliente.activo:
            return False, "Ese cliente ya está inactivo."
        cliente.activo = False
        return True, "Cliente marcado como inactivo correctamente."

    # --- Siembra inicial de clientes (hardcodeado) ---
    def _sembrar_clientes_iniciales(self):
        # Puedes modificar estos datos si quieres que sean otros
        datos = [
            ("Ana", "Pérez", "3001234567"),
            ("Luis", "Gómez", "3017654321"),
            ("María", "Rojas", "3025556677"),
            ("Carlos", "Torres", "3031112233"),
            ("Daniela", "Martínez", "3044445566"),
        ]
        for nombre, apellido, tel in datos:
            self.registrar_cliente(nombre, apellido, tel)

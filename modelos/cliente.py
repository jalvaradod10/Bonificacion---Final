# modelos/cliente.py
# Representa un cliente. Eliminación lógica con bandera "activo".

class Cliente:
    def __init__(self, id_cliente, nombre, apellido, telefono):
        self.id = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.activo = True  # si se “elimina”, pasa a False

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}".strip()

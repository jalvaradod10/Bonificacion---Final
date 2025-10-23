class Cliente:
    def __init__(self, id_cliente, nombre, apellido, telefono):
        self.id = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.activo = True 

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}".strip()

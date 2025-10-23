from validacion.validacion import leer_entero, leer_no_vacio

def imprimir_menu():
    print("\n===== MENÚ =====")
    print("1. Registrar un cliente")
    print("2. Listar clientes")
    print("3. Eliminar un cliente (lógico)")
    print("4. Salir")

def flujo_registrar_cliente(sistema):
    print("\n> Registrar cliente")
    nombre = leer_no_vacio("Nombre: ")
    apellido = leer_no_vacio("Apellido: ")
    telefono = leer_no_vacio("Teléfono: ")
    c = sistema.registrar_cliente(nombre, apellido, telefono)
    print(f"✔ Cliente registrado con ID {c.id}: {c.nombre_completo()} — Tel: {c.telefono}")

def flujo_listar_clientes(sistema):
    print("\n> Listado de clientes")
    if sistema.cantidad_clientes() == 0:
        print("No hay clientes registrados.")
        return

    print(f"{'ID':<5} {'Nombre':<25} {'Teléfono':<15} {'Estado'}")
    hay = False
    for c in sistema.iterar_clientes():
        hay = True
        estado = "Activo" if c.activo else "Inactivo"
        print(f"{c.id:<5} {c.nombre_completo():<25} {c.telefono:<15} {estado}")
    if not hay:
        print("(sin datos)")

def flujo_eliminar_cliente(sistema):
    print("\n> Eliminar cliente (lógico)")
    idc = leer_entero("ID del cliente a inactivar: ", minimo=1)
    ok, msg = sistema.eliminar_logico_cliente(idc)
    if ok:
        print("CORRECTO", msg)
    else:
        print("INCORRECTO", msg)

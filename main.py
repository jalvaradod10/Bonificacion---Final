from servicios.sistema import Sistema
from visual.menu import (
    imprimir_menu,
    flujo_registrar_cliente,
    flujo_listar_clientes,
    flujo_eliminar_cliente
)
from validacion.validacion import leer_entero

def main():
    sistema = Sistema()
    print("Clientes iniciales cargados. Usa la opción 2 para verlos.")
    opcion = 0
    while opcion != 4:
        imprimir_menu()
        opcion = leer_entero("Seleccione una opción: ", minimo=1, maximo=4)

        if opcion == 1:
            flujo_registrar_cliente(sistema)
        elif opcion == 2:
            flujo_listar_clientes(sistema)
        elif opcion == 3:
            flujo_eliminar_cliente(sistema)
        elif opcion == 4:
            print("Saliendo... ¡Gracias!")

if __name__ == "__main__":
    main()

def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        texto = input(mensaje).strip()
        if texto.isdigit():
            n = int(texto)
            if minimo is not None and n < minimo:
                print(f"→ Debe ser >= {minimo}")
                continue
            if maximo is not None and n > maximo:
                print(f"→ Debe ser <= {maximo}")
                continue
            return n
        print("→ Ingrese un número entero válido.")

def leer_no_vacio(mensaje):
    while True:
        s = input(mensaje).strip()
        if s:
            return s
        print("→ No puede estar vacío.")

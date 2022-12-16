opcion = 0
cantidad = 0
forma_pago = ""
comprobante = 0
ventas = []

def nueva_venta():
    """Funcion para crear venta"""
    opcion = elegir_menu()
    if opcion == 1:
        precio = 100
    elif opcion == 2:
        precio = 200
    elif opcion == 3:
        precio = 300

    cantidad = ingresar_cantidad()

    if cantidad > 1:
        precio = precio * cantidad

    forma_pago = ingresar_forma_pago()

    if(forma_pago == 'MP'):
        comprobante = ingresar_comprobante()
        ventas.append([opcion, cantidad, precio, forma_pago, comprobante])
    else:
        print("Por favor, no se olvide de pagar al retirar")
        print("")
        ventas.append([opcion, cantidad, precio, forma_pago])     

    finalizar_venta()
    
def elegir_menu():
    """Funcion para elegir menu"""
    while True:
        try:
            opcion = int(input("Ingrese opcion elegida: "))
            if opcion > 0 and opcion <= 3:
                return opcion
            else:
                print("Numero opcion debe ser mayor a 0")
        except:
            print("Numero opcion debe ser un valor numerico")
    

def ingresar_cantidad():
    """Funcion para ingresar cantidad"""
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser mayor a 0")
        except:
            print("La cantidad debe ser un valor numerico")

def ingresar_forma_pago():
    """Funcion para ingresar forma de pago"""
    while True:
        forma_pago = input("Ingrese forma de pago: EF (Efectivo) - MP (Mercado pago): ")
        forma_pago = forma_pago.upper()
        if forma_pago == 'EF' or forma_pago == 'MP':
            return forma_pago
        else:
            print("Ingrese un dato valido")

def ingresar_comprobante():
    """Funcion para ingresar comprobante"""
    while True:
        try:
            comp = int(input("Ingrese ultimos 5 digitos del comprobante: "))
            if len(str(comp)) == 5:
                return comp
            else:
                print("Debe ingresar 5 digitos")
        except:
            print("Se esperaba un valor numerico")

def finalizar_venta():
    """Funcion para finalizar venta"""
    print("Comprobante de pedido")
    for venta in ventas:
        if venta[3] == "EF":
            print("")
            print(f"Opcion: {venta[0]} | Cantidad: {venta[1]} | Forma de pago: {venta[3]} | Total pagado: {venta[2]}")
        else:
            print("")
            print(f"Opcion: {venta[0]} | Cantidad: {venta[1]} | Forma de pago: {venta[3]}| Comprobante {venta[4]} | Total pagado: {venta[2]}")
    print("")
    print("Gracias por su compra!")


def Menu():
    print("""------------------BUFFET LAS CANDELAS / MENU PRINCIPAL -------------------------------------
    
    Menu de hoy:
        Opcion 1: Pollo + Tomate + Coca = $100
        Opcion 2: Hamburguesa + Tomate + Coca = $200
        Opcion 3: Pescado + Banana + Coca = $300
        
    Selecciona una opción...
    1 - Comprar
    0 - Salir""")


# --------------- Programa principal----------------------------
while True:
    Menu()

    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion = -1

    # Comprar
    if opcion == 1:
        nueva_venta()
    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")
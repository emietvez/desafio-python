import random

ventasTotales = []
producto = ""
precio = 0.00
cantidad = 0
forma_pago = ""
carrito = []
agregar = ''


def menu_ventas():
    print("""------------------BUFFET LAS CANDELAS / VENTA -------------------------------------
        Selecciona una opción...
        1 - Agregar mas productos
        2 - Ver venta
        3 - Finalizar venta
        4 - Cancelar venta
        0 - Volver a menu principal""")


def nueva_venta():
    agregar_producto()
    while True:
        menu_ventas()

        try:
            opcion = int(input("Ingrese el número de la opción escogida: "))
        except:
            opcion = -1
        # Agregar mas productos
        if opcion == 1:
            agregar_producto()

        # Ver venta
        elif opcion == 2:
            ver_venta()

        # Finalizar venta
        elif opcion == 3:
            finalizar_venta()
            break
        
        # Cancelar venta
        elif opcion == 4:
            vaciar_carrito()
            print("""Venta cancelada""")

        elif opcion == 0:
            break
        else:
            print("La opción ingresada no es correcta, indica una opción correcta")


def agregar_producto():
    """Funcion para agregar productos"""
    agregar = ''
    respuesta = ''
    while agregar != 'NO' or agregar == 'SI':
        producto = input("Ingrese producto: ")
        precio = ingresar_precio()
        cantidad = ingresar_cantidad()

        if cantidad > 1:
            precio = precio * cantidad

        carrito.append([producto, precio, cantidad])

        respuesta = input("¿Quiere agregar mas productos? SI/NO \n")
        respuesta = respuesta.upper()
        if respuesta == 'SI' or respuesta == 'NO':
            agregar = respuesta
            respuesta = ''
        else:
            agregar = 'NO'
            print("Esta opcion no esa disponible")
            respuesta = ''


def ingresar_precio():
    """Funcion para ingresar precio"""
    while True:
        try:
            precio = float(input("Ingrese precio del producto: "))
            if 0 < precio:
                return precio
            else:
                print("El precio debe ser mayor a 0")
        except:
            print("El precio debe ser un valor numerico decimal")


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


def ver_venta():
    """Funcion para ver venta actual"""
    if (len(carrito) > 0):
        for item in carrito:
            print(
                f"Producto: {item[0]} | Precio: ${item[1]} | Cantidad: {item[2]}")
    else:
        print("No tiene productos en el carrito")

def finalizar_venta():
    """Funcion para finalizar venta"""
    if (len(carrito) > 0):

        total = 0

        for item in carrito:
            total += item[1]

        print(f"Total a pagar: ${total}")
        entrada = float(input("Ingrese pago: "))
        vuelto = entrada - total
        cod = random.randint(1, 1000)
        data_pago = forma_de_pago()

        if(data_pago == 'EF'):
            print(f'Cambio: ${vuelto} ')
            cart = carrito.copy()
            ventasTotales.append([cod, cart, data_pago, total])
        else:
           comprobante = ingresar_comprobante()
           cart = carrito.copy()
           ventasTotales.append([cod, cart, data_pago, total, comprobante])
        
        vaciar_carrito()

    else:
        print("No tiene productos en el carrito")

def forma_de_pago():
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

def vaciar_carrito():
    """Funcion para vaciar carrito actual"""
    carrito.clear()



def ventas_totales():
    """Funcion para ver ventas totales"""
    if(len(ventasTotales) > 0):
        for venta in ventasTotales:
            print("=========================================================================")
            if venta[2] == "EF":
                print(f"""Cod: {venta[0]} | Forma de pago: {venta[2]} | Total pagado: ${venta[3]}""")
            else:
                print(f"""Cod: {venta[0]} | Forma de pago: {venta[2]} | Total pagado: ${venta[3]} | Comprobante: {venta[4]}""")

            for item in venta[1]:
                print(f"""Producto: {item[0]} | Precio: ${item[1]} | Cantidad: {item[2]}""")
            print("=========================================================================")
    else:
        print("No hay ventas disponibles")



def ventas_efectivo():
    if(len(ventasTotales) > 0):
        print("VENTAS EN EFECTIVO")
        for venta in ventasTotales:
            if(venta[2] == "EF"):
                print("=========================================================================")
                print(f"""Cod: {venta[0]} | Forma de pago: {venta[2]} | Total pagado: ${venta[3]}""")
                for item in venta[1]:
                    print(f"""Producto: {item[0]} | Precio: ${item[1]} | Cantidad: {item[2]}""")
                print("=========================================================================")
            
    else:
        print("No hay ventas disponibles")


def ventas_mp():
    if(len(ventasTotales) > 0):
        print("VENTAS EN MERCADO PAGO")
        for venta in ventasTotales:
            if(venta[2] == "MP"):
                print("=========================================================================")
                print(f"""Cod: {venta[0]} | Forma de pago: {venta[2]} | Total pagado: ${venta[3]}""")
                for item in venta[1]:
                    print(f"""Producto: {item[0]} | Precio: ${item[1]} | Cantidad: {item[2]}""")
                print("=========================================================================")
            
    else:
        print("No hay ventas disponibles")


def Menu():
    print("""------------------BUFFET LAS CANDELAS / MENU PRINCIPAL -------------------------------------
    Selecciona una opción...
    1 - Nueva venta
    2 - Total vendido en efectivo
    3 - Total vendido en Mercado pago
    4 - Total ventas
    0 - Salir""")


# --------------- Programa principal----------------------------
while True:
    Menu()

    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion = -1

    # Agregar venta
    if opcion == 1:
        nueva_venta()
    # Ver ventas efectivo
    elif opcion == 2:
        ventas_efectivo()
    # Ver ventas Mercado pago
    elif opcion == 3:
        ventas_mp()
    # Ver ventas
    elif opcion == 4:
        ventas_totales()
    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")

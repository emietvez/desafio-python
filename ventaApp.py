opcion = 0
cantidad = 0
forma_pago = ""
comprobante = 0
carrito = []
ventas = []
user = []
alumno = [['Emiliano Estevez', 40725342]]
def validar_estudiante():
    
    dni = validar_dni()

    for i in alumno:
        if i[1] == dni:
            nueva_venta()
            user = alumno
        else:
            print("Alumno no encontrado")
            
    
def validar_dni():
    data = int(input("Ingrese dni de alumno para comprar: "))
 
    if len(str(data)) > 0 and len(str(data)) <= 8:
        return data
    else:
        print("Ingrese un dni valido")
def nueva_venta():
    """Funcion para crear venta"""
    agregar = ''
    respuesta = ''
    while agregar != 'NO' or agregar == 'SI':
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

        
        carrito.append([opcion, cantidad, precio])  

        total = total_pagar()
        print(f"Total a pagar ${total}")
        
        respuesta = input("¿Quiere agregar mas productos? SI/NO \n")
        respuesta = respuesta.upper()
        if respuesta == 'SI' or respuesta == 'NO':
            agregar = respuesta
            respuesta = ''
        else:
            agregar = 'NO'
            print("Esta opcion no esa disponible")
            respuesta = ''

    finalizar_venta()
   


def total_pagar():
    suma = 0
    for item in carrito:
        suma = suma + item[2]
    return suma

def elegir_menu():
    """Funcion para elegir menu"""
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion > 0 and opcion <= 3:
                return opcion
            else:
                print("Numero opcion debe ser mayor a 0 ")
        except:
            print("Numero opcion debe ser un valor numerico y no puede ser texto")
    

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
    total = 0
    user = alumno
    for item in carrito:
        total += item[2]

    print(f"Total a pagar: ${total}")
    
    data_pago = ingresar_forma_pago()

    if(data_pago == 'EF'):
        entrada = float(input("Ingrese con cuanto paga: "))
        vuelto = entrada - total
        print(f'Cambio: ${vuelto} ')
        cart = carrito.copy()
        ventas.append([cart, data_pago, total, vuelto, user])
    else:
        comprobante = ingresar_comprobante()
        cart = carrito.copy()
        ventas.append([cart, data_pago, total, comprobante, user])
    
    print(ventas)
    
    vaciar_carrito()
    mostrar_venta()

def vaciar_carrito():
    """Funcion para vaciar carrito actual"""
    carrito.clear()
def mostrar_venta():
    for venta in ventas:
        
        print("=========================================================================")
        if venta[1] == "EF":
            print(f""" Forma de pago: {venta[1]} | Total: ${venta[2]} | Cambio: ${venta[3]} """)
        else:
            print(f""" Forma de pago: {venta[1]} | Total: ${venta[2]} | Comprobante: {venta[3]}""")

        for item in venta[0]:
            print(f"""Menu: {item[0]} | Cantidad: {item[1]} | Precio: ${item[2]}""")
        print("=========================================================================")
        for j in venta[4]:
            print(f"Gracias por su compra {j[0]}")

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
        validar_estudiante()
    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")
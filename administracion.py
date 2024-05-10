from menus import*
import uuid

def codigo_unico():
    codigo= str(uuid.uuid4())
    return codigo
#clientes
def registrar_clientes(datos):
    datos= dict(datos)
    cliente ={}
    print("-------------------------------------------------------------------------")
    cliente["nombre"]= input("Ingresa el nombre del cliente: ")
    cliente["codigo"]= codigo_unico()
    print("El codigo unico del cliente es "+cliente["codigo"])
    cliente["email"]= input("Ingresa un email valido del cliente: ")
    telefono= input("Ingresa el telefono del cliente: ")
    while not len(telefono) == 10:
        print("Numero de telefono invalido")
        telefono= input("Ingresa el telefono del cliente: ")
    
    cliente["telefono"]= telefono
    cliente["ciudad"]= input("Ingresa la ciudad donde vive: ")
    cliente["direccion"]= input("Ingresa la direccion del cliente: ")
    cliente["compras"]= 0
    cliente["adquiridos"]= []

    datos["clientes"].append(cliente)
    print ("Cliente cargado!, cierra el programa para ver los cambios")
    return datos

def actualizar_clientes(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    usuario= input("Ingresa el codigo del cliente a cambiar: ")
    for i in range(len(datos["clientes"])):
        if usuario== datos["clientes"][i]["codigo"]:
            while True: 
                print("Que datos quieres actualizar\n1.Nombre\n2.Codigo\n3.Email\n4.Telefono\n5.Ciudad\n6.Direccion\n7.Salir")
                opcion= opc()
                while opcion not in [1,2,3,4,5,6,7]:
                    print("Ingresa una opcion valida\n")
                    opcion =opc()
                if opcion==1:
                    datos["clientes"][i]["nombre"]= input("Ingrese el nuevo nombre del cliente: ")
                    print("guardado!")
                elif opcion==2:
                        codigo_nuevo= datos["clientes"][i]["codigo"]= codigo_unico()
                        print("guardado!")
                        print("El codigo nuevo del cliente "+codigo_nuevo)
                elif opcion==3:
                        datos["clientes"][i]["email"]= input("Ingrese el nuevo email del cliente: ")
                        print("guardado!")
                elif opcion==4: 
                        telefono= input("Ingresa el telefono del cliente: ")
                        while not len(telefono) == 10:
                            print("Numero de telefono invalido")
                            telefono= input("Ingresa el telefono del cliente: ")
                        datos["clientes"][i]["telefono"]=telefono
                        print("guardado!")
                elif opcion==5:
                    datos["clientes"][i]["ciudad"]= input("Ingrese la nueva ciudad del cliente: ")
                    print("guardado!")
                elif opcion==6:
                    datos["clientes"][i]["direccion"]= input("Ingrese la nueva direccion del cliente: ")
                    print("guardado!")
                else:
                    print("Saliste de actualizar clientes!")
                    break
    return datos

def eliminar_usuario(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    usuario= input("Ingresa el codigo del cliente a eliminar: ")
    for i in range(len(datos["clientes"])):
        if usuario== datos["clientes"][i]["codigo"]:
            datos["clientes"].pop(i)
            print("Usuario eliminado!")
            return datos
    return datos

def listar_usuarios(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de clientes\n")
    for i in range(len(datos["clientes"])):
        print(str(indice)+"."+" Nombre: " + datos["clientes"][i]["nombre"]+ " - "+ "Codigo: "+datos["clientes"][i]["codigo"])
        print("")
        indice+=1

#servicios
def registrar_servicios(datos):
    datos= dict(datos)
    servicio ={}
    print("-------------------------------------------------------------------------")
    servicio["nombre_serv"]= input("Ingresa el nombre del servicio: ")
   

    servicio["codigo"]= codigo_unico()
    print("El codigo unico del servicio es "+ servicio["codigo"])
    servicio["categoria"]= input("Ingresa la categoria del servicio: ")
    servicio["descripcion"]= input("Ingresa la descripcion del servicio: ")
    servicio["precio"]= input("El precio del servicio: ")


    datos["servicios"].append(servicio)
    print ("Servicio listo!, cierra el programa para ver los cambios")
    return datos

def actualizar_servicios(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    codigo_serv= input("Ingresa el codigo del servicio a cambiar: ")
    for i in range(len(datos["servicios"])):
        if codigo_serv== datos["servicios"][i]["codigo"]:
            while True: 
                print("Que datos quieres actualizar\n1.Nombre\n2.Codigo\n3.Categoria\n4.Descripcion\n5.Precio\n6.Salir")
                opcion= opc()
                while opcion not in [1,2,3,4,5,6]:
                    print("Ingresa una opcion valida\n")
                    opcion =opc()
                if opcion==1:
                    datos["servicios"][i]["nombre_serv"]= input("Ingrese el nuevo nombre del servicio: ")
                    print("guardado!")
                elif opcion==2:
                        codigo_nuevo= datos["servicios"][i]["codigo"]= codigo_unico()
                        print("guardado!")
                        print("El codigo nuevo del servicio es "+codigo_nuevo)
                elif opcion==3:
                        datos["servicios"][i]["categoria"]= input("Ingrese la nueva categoria del servicio: ")
                        print("guardado!")
                elif opcion==4:
                    datos["servicios"][i]["descripcion"]= input("Ingrese la nueva descripcion del servicio: ")
                    print("guardado!")
                elif opcion==5:
                    datos["servicios"][i]["precio"]= input("Ingrese el precio actualizado del servicio: ")
                    print("guardado!")
                else:
                    print("Saliste de actualizar servicios!")
                    break
    return datos

def eliminar_servicio(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    servicio= input("Ingresa el codigo del servicio a eliminar: ")
    for i in range(len(datos["clientes"])):
        if servicio== datos["servicios"][i]["codigo"]:
            datos["servicios"].pop(i)
            print("Servicio eliminado!")
            return datos
    return datos

def listar_servicios(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de servicios\n")
    for i in range(len(datos["servicios"])):
        print(str(indice)+"."+" Nombre: " + datos["servicios"][i]["nombre_serv"]+ " - "+ "Codigo: "+datos["servicios"][i]["codigo"])
        print("")
        indice+=1

#productos 
def registrar_productos(datos):
    datos= dict(datos)
    producto ={}
    print("-------------------------------------------------------------------------")
    producto["nombre"]= input("Ingresa el nombre del producto: ")
    producto["codigo"]= codigo_unico()
    print("El codigo unico del producto es "+producto["codigo"])
    producto["categoria"]= input("Ingresa la categoria del producto: ")
    producto["marca"]= input("Ingresa la marca del producto: ")
    producto["caracteristicas"]= input("Ingresa las caracteristicas del producto: ")
    producto["garantia"]= input("Ingresa la duracion de garantia del producto: ")
    producto["precio"]= input("Ingresa el precio del producto: ")


    datos["productos"].append(producto)
    print ("Producto listo!, cierra el programa para ver los cambios")
    return datos

def actualizar_productos(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    codigo_producto= input("Ingresa el codigo del producto a cambiar: ")
    for i in range(len(datos["productos"])):
        if codigo_producto== datos["productos"][i]["codigo"]:
            while True: 
                print("Que datos quieres actualizar\n1.Nombre\n2.Codigo\n3.Marca\n4.Categoria\n5.Caracteristicas\n6.Garantia\n7.Precio\n8.Salir")
                opcion= opc()
                while opcion not in [1,2,3,4,5,6,7,8]:
                    print("Ingresa una opcion valida\n")
                    opcion =opc()
                if opcion==1:
                    datos["productos"][i]["nombre"]= input("Ingrese el nuevo nombre del producto: ")
                    print("guardado!")
                elif opcion==2:
                    codigo_nuevo= datos["productos"][i]["codigo"]= codigo_unico()
                    print("guardado!")
                    print("El codigo nuevo del servicio es "+codigo_nuevo)
                elif opcion==3:
                        datos["productos"][i]["marca"]= input("Ingrese la nueva marca del producto: ")
                        print("guardado!")
                elif opcion==4:
                    datos["productos"][i]["categoria"]= input("Ingrese la nueva categoria del producto: ")
                    print("guardado!")
                elif opcion==5:
                    datos["productos"][i]["caracteristicas"]= input("Ingrese las caracteristicas actualizadas del producto: ")
                    print("guardado!")
                elif opcion==6:
                    datos["productos"][i]["garantia"]= input("Ingrese la nueva garantia del producto: ")
                    print("guardado!")
                elif opcion==7:
                    datos["productos"][i]["precio"]= input("Ingrese el precio actualizado del producto: ")
                    print("guardado!")
                else:
                    print("Saliste de actualizar productos!")
                    break
        return datos
    
def eliminar_producto(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    producto= input("Ingresa el codigo del producto a eliminar: ")
    for i in range(len(datos["clientes"])):
        if producto== datos["productos"][i]["codigo"]:
            datos["productos"].pop(i)
            print("Producto eliminado!")
            return datos
    return datos

def listar_productos(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de productos\n")
    for i in range(len(datos["productos"])):
        print(str(indice)+"."+" Nombre: " + datos["productos"][i]["nombre"]+ " - "+ "Codigo: "+datos["productos"][i]["codigo"])
        print("")
        indice+=1

#usuarios
def registrar_compra(datos):
    datos= dict(datos)
    codigo= input("Ingresa tu codigo personal de cliente Claro: ")
    for i in range(len(datos["clientes"])):
        if codigo == datos["clientes"][i]["codigo"]:
            print("¿Que deseas adquirir?:\n1.Servicios\n2.Productos\n3.Salir")
            opcion=opc()
            while not opcion in [1,2,3]:
                opcion =opc()
                print("Escoge una opcion valida\n")
            if opcion==1:
                #marca excepcion
                cantidad_compra= int(input("Ingresa la cantidad del servicio que vas a adquirir: "))
                if cantidad_compra==0:
                    break
                codigo_servicio= input("Ingresa el codigo del servicio que vas a adquirir: ")
                for servicio in datos["servicios"]:
                    if codigo_servicio== servicio["codigo"]:
                        compras_anteriores= datos["clientes"][i]["compras"]
                        compras_totales= cantidad_compra + compras_anteriores
                        servicio_comprado= servicio["nombre_serv"]

                        datos["clientes"][i]["compras"]= compras_totales
                        datos["clientes"][i]["adquiridos"].append(servicio_comprado)
                        print("Gracias!, tu compra fue realizada")
            elif opcion==2:
                #marca excepcion
                cantidad_compra= int(input("Ingresa la cantidad del producto que vas a adquirir: "))
                if cantidad_compra==0:
                    break
                codigo_producto= input("Ingresa el codigo del producto que vas a adquirir: ")
                for producto in datos["productos"]:
                    if codigo_producto== producto["codigo"]:
                        compras_anteriores= datos["clientes"][i]["compras"]
                        compras_totales= cantidad_compra + compras_anteriores
                        producto_comprado= producto["nombre"]

                        datos["clientes"][i]["compras"]= compras_totales
                        datos["clientes"][i]["adquiridos"].append(producto_comprado)
                        print("Gracias!, tu compra fue realizada")
            else:
                print("Saliste de Adquiere los productos Claro!")
    return datos

def encuesta_publicidad():
    celulares= 0
    hogar= 0
    computadores=0
    streaming=0
    servicio_movil=0


    print("Bienvenido a la encuesta de preferencias Claro!".center(60)) 
    print("En Claro nos esforzamos por brindarte servicios y productos que se adapten perfectamente a tus necesidades y preferencias. Para asegurarnos de que recibas la mejor experiencia posible, nos gustaría conocer más sobre ti y tus intereses, debes terminar la encuesta hasta el final ¡Empecemos!")
    print("1. ¿Que edad tienes?\n1. 18-25 años\n2. 26-35 años\n3. 36-45 años \n4. Mayor de 45 años")
    opcion= opc()
    while not opcion in [1,2,3,4]:
        opc()
        print("Opcion incorrecta, elige una valida!")
    if opcion==1:
        celulares+=2
        computadores+=2
        streaming+=2
        servicio_movil+=2
    elif opcion==2 or opcion==3:
        celulares+=2
        computadores+=2
        streaming+=2
        servicio_movil+=2
        hogar+=2
    else:
        celulares+=1
        computadores+=1
        streaming+=2
        servicio_movil+=2
        hogar+=2

    print("2.¿Con qué frecuencia usas servicios de streaming de video?\n1. Diariamente\n2. Una vez por semana\n3. Varias veces al mes  \n4. Casi nunca")
    opcion= opc()
    while not opcion in [1,2,3,4]:
        opc()
        print("Opcion incorrecta, elige una valida!")
    if opcion==1:
        streaming+=3
    elif opcion==2: 
        streaming+=2
    elif opcion==3:
        streaming+=1   
    else:
        streaming=streaming
    
    print("2.¿Con qué frecuencia usas servicios de streaming de video?\n1. Diariamente\n2. Una vez por semana\n3. Varias veces al mes  \n4. Casi nunca")
    opcion= opc()
    while not opcion in [1,2,3,4]:
        opc()
        print("Opcion incorrecta, elige una valida!")
    if opcion==1:
        streaming+=3
    elif opcion==2: 
        streaming+=2
    elif opcion==3:
        streaming+=1   
    else:
        streaming=streaming

    print("3. ¿Cuánto tiempo pasas en tus dispositivos móviles al día?\n 1. Menos de 1 hora\n2. 1-2 horas\n3. 2-4 horas\n4. Más de 6 horas")
    opcion= opc()
    while not opcion in [1,2,3,4]:
        opc()
        print("Opcion incorrecta, elige una valida!")
    if opcion==1:
        servicio_movil+=1
    elif opcion==2: 
        servicio_movil+=2
    elif opcion==3:
        servicio_movil+=3
    else:
        servicio_movil+=4

    
        
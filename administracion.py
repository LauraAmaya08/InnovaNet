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
        else:
             print("Usuario no hallado")
    return datos

def listar_usuarios(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de clientes\n")
    for i in range(len(datos["clientes"])):
        print(str(indice)+"."+datos["clientes"][i]["nombre"]+ "-"+ datos["clientes"][i]["codigo"])
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
        else:
             print("Servicio no hallado")
    return datos

def listar_servicios(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de servicios\n")
    for i in range(len(datos["servicios"])):
        print(str(indice)+"."+datos["servicios"][i]["nombre_serv"]+ "-"+ datos["servicios"][i]["codigo"])
        print("")
        indice+=1

#productos 
def registrar_productos(datos):
    datos= dict(datos)
    producto ={}
    print("-------------------------------------------------------------------------")
    producto["nombre"]= input("Ingresa el nombre del producto: ")


    codigo= input("Ingresa el codigo del producto: ")
    for i in range(len(datos["productos"])):
        while codigo ==datos["productos"][i]["codigo"]:
            print("codigo repetido")
            codigo= input("Ingresa el codigo del producto: ")

    producto["codigo"]= codigo_unico()
    print("El codigo unico del producto es "+producto["codigo"])
    producto["categoria"]= input("Ingresa la categoria del producto: ")
    producto["marca"]= input("Ingresa la marca del producto: ")
    producto["caracteristicas"]= input("Ingresa las caracteristicas del producto: ")
    producto["garantia"]= input("Ingresa la duracion de garantia del producto: ")
    producto["precio"]= input("Ingresa el precio del producto: ")


    datos["productos"].append(producto)
    print ("Servicio listo!, cierra el programa para ver los cambios")
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
                        codigo_nuevo= datos["servicios"][i]["codigo"]= codigo_unico()
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
        else:
             print("Producto no hallado")
    return datos

def listar_productos(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de productos\n")
    for i in range(len(datos["productos"])):
        print(str(indice)+"."+datos["productos"][i]["nombre"]+ "-"+ datos["productos"][i]["codigo"])
        print("")
        indice+=1
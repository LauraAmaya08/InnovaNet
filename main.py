from menus import*
from manejo_json import*
from administracion import*

datos= cargar("Innovanet.json")
#menu principal
while True:
    menu_principal()
    opcion= opc()
    while opcion not in [1,2,3]:
            opcion =opc()
            print("Ingresa una opcion valida\n")
#clientes
    if opcion==1:
            while True:
                print("")
                menu_cliente()
                opcion=opc()
                while opcion not in [1,2,3,4,5,6]:
                    opcion =opc()
                    print("Ingresa una opcion valida\n")
                if opcion==1:
                    print("opcion1")
                elif opcion== 2:
                    print("opcion2")
                elif opcion== 3:
                    print("opcion3")
                elif opcion== 4:
                    print("opcion4")
                elif opcion== 5:
                    print("opcion5")
                else:
                    print("Decidiste salir del Portal de Usuarios,adios!")
                    break
#administrativos
    elif opcion==2:
            while True:
                print("")
                menu_admin()
                opcion= opc()
                while opcion not in [1,2,3,4,5]:
                    opcion =opc()
                    print("Ingresa una opcion valida\n")
#usuarios
                if opcion==1:
                    print("")
                    admin_usuarios()
                    opcion= opc()
                    while opcion not in [1,2,3,4,5,6,7,8]:
                        opcion =opc()
                        print("Ingresa una opcion valida\n")
                    if opcion==1:
                        datos = registrar_clientes(datos)
                    elif opcion== 2:
                        datos= actualizar_clientes(datos)
                    elif opcion== 3:
                        datos= eliminar_usuario(datos)
                    elif opcion== 4:
                        listar_usuarios(datos)
                    elif opcion== 5:
                        print("opcion5")
                    elif opcion== 6:
                        print("opcion6")
                    elif opcion== 7:
                        print("opcion7")
                    else:
                        print("Decidiste salir de Usuarios, adios!")
#Servicios y productos
                elif opcion== 2:
                    print("")
                    productos_servicios()
                    opcion= opc()
                    while opcion not in [1,2,3]:
                        opcion =opc()
                        print("Ingresa una opcion valida\n")
#servicios
                    if opcion==1:
                        print("")
                        admin_servicios()
                        opcion= opc()
                        while opcion not in [1,2,3,4,5]:
                            opcion =opc()
                            print("Ingresa una opcion valida\n")
                        if opcion==1:
                            datos= registrar_servicios(datos)
                        elif opcion== 2:
                            datos= actualizar_servicios(datos)
                        elif opcion==3: 
                            datos= eliminar_servicio(datos)
                        elif opcion ==4:
                            listar_servicios()
                        else:
                            print("Decidiste salir de Servicios!")
#productos                        
                    elif opcion== 2:
                        print("")
                        admin_productos()
                        opcion= opc()
                        while opcion not in [1,2,3,4,5]:
                            opcion =opc()
                            print("Ingresa una opcion valida\n")
                        if opcion==1:
                            datos= registrar_productos(datos)
                        elif opcion== 2:
                            datos= actualizar_productos(datos)
                        elif opcion==3: 
                            datos= eliminar_producto(datos)
                        elif opcion==4:
                            listar_productos()
                        else:
                            print("Decidiste salir de Productos!")
                        
                    else:
                        print("Decidiste salir Productos y Servicios, adios!")
#reportes
                elif opcion== 3:
                    print("")
                    reportes()
                    opcion= opc()
                    while opcion not in [1,2,3,4]:
                        opcion =opc()
                        print("Ingresa una opcion valida\n")
                    if opcion==1:
                        print("opcion1")
                    elif opcion== 2:
                        print("opcion2")
                    elif opcion==3: 
                        print("opcion3")
                    else:
                        print("Decidiste salir de Reportes, adios!")
#ventas
                elif opcion== 4:
                    print("")
                    ventas()
                    opcion= opc()
                    while opcion not in [1,2,3,4]:
                        opcion =opc()
                        print("Ingresa una opcion valida\n")
                    if opcion==1:
                        print("opcion1")
                    elif opcion== 2:
                        print("opcion2")
                    elif opcion==3: 
                        print("opcion3")
                    else:
                        print("Decidiste salir de Ventas, adios!")
                else:
                    print("Decidiste salir del Sistema de Gestion y Ventas,adios!")
                    break
    else:
         print("Decidiste salir del programa!")
         break





datos= guardar(datos,"Innovanet.json")

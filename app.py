from funciones import *
import json




def menu()->str: #Esta funcion no retorna un string, no retorna nada
    print("\nMenu de opciones:")
    print("1. Cargar archivo CSV")
    print("2. Imprimir lista")
    print("3. Asignar estadisticas")  
    print("4. Filtrar por mejores posts")  
    print("5. Filtrar por haters")
    print("6. Informar promedio de followers")
    print("7. Ordenar los datos por nombre de user ascendente")
    print("8. Mostrar más popular")
    print("9. Salir\n")

#no es particularmente necesaria esta funcion, podrias simplemente declarar que estas 2 banderas son falsas, ademas seria mejor usar nombres mas claros, no me es claro todavia que hacen estas 2 banderas. Tambien las consignas del parcial especificaban que todas las funciones tienen que estar en un archivo aparte
def redes_app():
    bandera_3 = False
    bandera_1 = False

#en vez de un while True, te recomiendo usar una bandera con un nombre similar a desea_continuar o algo asi, y que en la opcion de salir esa variable sea cambiada a False; es una buena practica y el profe le da mucha bola a eso
    while True:

        menu()
        aux = input("Ingrese la opción deseada: ")
        opcion = int(aux) #no es realmente necesario convertir el input a un entero, ya que no se realiza ningun tipo de operacion matematica con esta variable, el match case se puede hacer con strings. Es mas, la existencia de esta linea te genera un error gravisimo en el codigo: intentas convertir un string a un int sin antes validar que este elemento pueda ser convertido a string. Si el input es cualquier tipo de caracter no numerico o un string vacio, el programa se rompe.

        match opcion:
            case 1:
                # Otro while true. Igualmente este punto funciona genial, sin embargo te recomiendo mucho mas hacer loops usando banderas con nombres claros, por ej nombre_invalido. En este caso al leer "while nombre_invalido" se sabe instantaneamente que el proposito del loop es la validacion del nombre 
                while True:
                    nombre_archivo = input("Ingrese el nombre del archivo a cargar: ")
                    try:
                        with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
                            encabezado = archivo.readline().strip("\n").split(",")

                            lineas = archivo.readlines()
                            # esto lo puedo recorrer para armar el diccionario

                            lista_posts = []

                            for linea in lineas:
                                post = {}

                                linea = linea.strip("\n").split(",")

                                id, user, likes, dislikes, followers = linea
                                post["id"] = int(id)
                                post["user"] = user
                                post["likes"] = int(likes)
                                post["dislikes"] = int(dislikes)
                                post["followers"] = int(followers)
                                lista_posts.append(post)
                            
                            
                            print("El archivo se cargó con éxito")
                        bandera_1 = True #seria mucho mejor que esta bandera se llame archivo_cargado para facilitar la legibilidad del codigo, tanto para vos como para otros que lo esten leyendo
                        break
                    except: #aca podrias especificar fileNotFoundError, pero no es del todo necesario
                        print("El nombre del archivo es incorrecto o no existe. Por favor intente de nuevo.")

            case 2:
                    if bandera_1:
                        mostrar_posteos(lista_posts)
                    else:
                        print("Primero debe ingresar un archivo")
            case 3: # Estaria mejor que reemplazes los valores de lista_posts en lugar de crear la nueva lista_estadisticas: esto permitiria ver las estadisticas asignadas en la segunda opcion. Como esta ahora el programa, no hay manera de ver dichas estadisticas. Es posible que esto haya sido visto como un error por el profe
                    if bandera_1:
                        lista_estadisticas = mapear_lista(lista_posts)
                        bandera_3 = True #otra bandera con un nombre ambiguo, seria mejor que se llame estadisticas_cargadas. Ademas el hecho de que tus dos banderas sean bandera_1 y bandera_3 es un poco confuso
                    else:
                        print("Primero debe ingresar un archivo")
            case 4:
                    if bandera_3:
                        mejores_posteos = filtrar_lista(lambda post: post["likes"] > 2000, lista_estadisticas)

                        with open(get_path_actual("mejores_posteos.csv"),"w", encoding="utf-8") as archivo:
                            encabezado = ",".join(list(mejores_posteos[0].keys())) + "\n"

                            archivo.write(encabezado)
                            
                            for post in mejores_posteos:
                                values = list(post.values())
                                l = []

                                for value in values:
                                    if isinstance(value, int):
                                        l.append(str(value))
                                    elif isinstance(value, float):
                                        l.append(str(value))
                                    else:
                                        l.append(value)
                                        
                                linea = ",".join(l) + "\n"
                                archivo.write(linea)
                    else:
                        print("Primero debe cargar estadisticas")
            case 5:
                    if bandera_3:
                        filtrar_haters = filtrar_lista(lambda post: post["dislikes"] > post["likes"], lista_estadisticas)   
                        with open(get_path_actual("haters.csv"),"w", encoding="utf-8") as archivo:
                            encabezado = ",".join(list(filtrar_haters[0].keys())) + "\n"

                            archivo.write(encabezado)
                            
                            for post in filtrar_haters:
                                values = list(post.values())
                                l = []

                                for value in values:
                                    if isinstance(value, int):
                                        l.append(str(value))
                                    elif isinstance(value, float):
                                        l.append(str(value))
                                    else:
                                        l.append(value)
                                        
                                linea = ",".join(l) + "\n"
                                archivo.write(linea)
                    else:
                        print("Primero debe cargar estadisticas")


            case 6:
                    if bandera_3:
                        campo = "followers"
                        promedio_campo(lista_estadisticas,campo)
                    else:
                        print("Primero debe ingresar un archivo")
            case 7:
                    if bandera_3:
                        ordenar_lista(lambda a, b: a["user"] > b["user"], lista_estadisticas)

                        with open(
                            get_path_actual("user_ascendente.json"), "w", encoding="utf-8"
                        ) as archivo:
                            json.dump(lista_estadisticas, archivo, indent=4)
                    else:
                        print("Primero debe ingresar un archivo")

            case 8:
                if bandera_3:
                    user_popular= reduce_lista(lambda ant, act: act if ant['likes'] < act['likes'] else ant, lista_estadisticas)
                    print(f"El user {user_popular["user"]} tiene el posteo más likeado con {user_popular["likes"]} likes")
                else:
                    print("Primero debe ingresar un archivo")

            case 9:
                print("Saliendo de la aplicación")
                break
            
            case _:
                print("La opción no es válida. Intenta de nuevo.")

    print("Fin del programa")

redes_app() # no es necesaria esta funcion, lo unico que hace aca es cambiar el valor de tus dos banderas. La razon por la que esto no tiene proposito es porque esta en la ultima linea antes de que se termine de ejecutar el programa. Nada va a volver a leer estas variables y al volver a ejecutar el programa, este no recuerda lo hecho en esta linea, comienza otra vez de 0





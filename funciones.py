# falta documentacion en todas las funciones, lo cual era un requisito para la aprobacion

def get_path_actual(nombre_archivo):
    import os

    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual,nombre_archivo)


def validar_lista(lista: list) -> None:
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista.")
    
def sumar_lista(lista: list) -> int: 
    suma = 0
    validar_lista(lista)
    for i in lista:
        suma += i

    return suma

def calcular_promedio(lista: list) -> float: #esta funcion y la anterior no son necesarias cuando ya tenes reduce,podrias conseguir la sumatoria usando reduce y dividirla por el len de la lista, ahorrandote las lineas de codigo en estas 2 funciones
    validar_lista(lista)
    # Validación dentro de la función
    if len(lista) != 0:
        promedio = sumar_lista(lista) / len(lista)
        return promedio
    else:
        return "No se puede dividir por 0"


def mostrar_posteos(posteos: list) -> None:

    validar_lista(posteos)

    print("         ***Lista de Posteos***             ") 
    print("    Id         User             Likes    Dislikes   Followers")
    print("----------------------------------------------------------------------")

    for i in range(len(posteos)):
        mostrar_post_item(posteos[i])

# Imprime empleado en una linea
def mostrar_post_item(post: dict) -> None:
    print(
        f"{post["id"]:>4} {post["user"]:>20}    {post["likes"]:>6}    {post["dislikes"]:8}   {post["followers"]:6}"
    )


def mapear_lista(lista:list)->list:
    from random import randint

    validar_lista(lista)

    lista_retorno = []

    LIKES_MIN = 500
    LIKES_MAX = 3000
    DISLIKES_MIN= 300
    DISLIKES_MAX = 3500
    FOLLOWERS_MIN = 10000
    FOLLOWERS_MAX = 20000
    
    for el in lista:
        post = {}
        likes = randint(LIKES_MIN,LIKES_MAX)
        dislikes = randint(DISLIKES_MIN,DISLIKES_MAX)
        followers = randint(FOLLOWERS_MIN,FOLLOWERS_MAX)

        post["id"] = (el["id"])
        post["user"]= (el["user"])
        post["likes"]= likes
        post["dislikes"] = dislikes
        post["followers"] = followers

        lista_retorno.append(post)

    return lista_retorno

def mapear_campo(lista:list, campo:str)->None:
    validar_lista(lista)
    lista_retorno = []

    for post in lista:
        lista_retorno.append(post[campo])

    return lista_retorno

def filtrar_lista(filtradora, lista: list)->list:
    validar_lista(lista)
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada


def promedio_campo(lista:list, campo:str): #el nombre de esta funcion implica que algo se esta promediando, cuando lo que realmente hace es mostrar un dato por consola
    validar_lista(lista)
    resultado = mapear_campo(lista,campo)
        
    print(f"El promedio de {campo} es {calcular_promedio(resultado):.0f}")

def swap_lista(lista: list, i: int, j: int) -> None:
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_lista(comparator, lista: list) -> None:
    tam = len(lista)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if comparator(lista[i], lista[j]):
                swap_lista(lista, i, j)


def reduce_lista(funcion, lista, valor_inicial = None):
    tam = len(lista)
    if tam == 0:
        raise ValueError("Error. Lista vacia")
    
    if valor_inicial:
        ant = valor_inicial
        indice = 0
    else:
        ant = lista[0]
        indice = 1

    for act in lista[indice:]:
        ant = funcion(ant,act)
    
    return ant

def mostrar_lista_tuplas(lista:list)->None:
    for tupla in lista:
        for elemento in tupla:
            print(f"{elemento:15}",end="")
        print()
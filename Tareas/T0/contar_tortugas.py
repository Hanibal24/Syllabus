
def tortugas (tablero: list):
    n , lista= len(tablero) , []
    for i in range(n):
            pos = 0
            for j in range(n):
                x = str(tablero[i][j])
                if x == "T":
                     lista.append(tablero[i][j])
    return lista
     

def contar_derecha_tortuga (tablero: list):
    n , lista_tope = len(tablero) , []
    for i in range(n):
            pos = 0
            for j in range(n):
                contar , caracter = 0 , tablero[i][j] 
                if caracter == "T":
                    for k in range(n-pos):
                        filtrador = tablero[i][pos+k]
                        if filtrador == "T" and k == 1:
                             contar += 1
                        else:
                             contar = contar
          
                    if contar == 1:
                        lista_tope.append(contar)
                    else: 
                        lista_tope.append(contar)
                pos += 1
    return lista_tope


def contar_izquierda_tortuga (tablero: list):
    n , lista_tope = len(tablero) , []
    for i in range(n):
            pos = 0
            for j in range(n):
                contar , caracter = 0 , tablero[i][j] 
                if caracter == "T":
                    for k in range(pos+1):
                        filtrador = tablero[i][pos-k]
                        if filtrador == "T" and k == 1:
                             contar += 1
                        else:
                             contar = contar
          
                    if contar == 1:
                        lista_tope.append(contar)
                    else: 
                        lista_tope.append(contar)
                pos += 1
    return lista_tope


def contar_arriba_tortuga (tablero: list):
    n , lista_tope = len(tablero) , []
    for i in range(n):
            pos = 0
            for j in range(n):
                contar , caracter = 0 , tablero[i][j] 
                if caracter == "T":
                    for k in range(i+1):
                        filtrador = tablero[i-k][j]
                        if filtrador == "T" and k == 1:
                             contar += 1
                        else:
                             contar = contar
          
                    if contar == 1:
                        lista_tope.append(contar)
                    else: 
                        lista_tope.append(contar)
                pos += 1
    return lista_tope


def contar_abajo_tortuga (tablero: list):
    n , lista_tope = len(tablero) , []
    for i in range(n):
            pos = 0
            for j in range(n):
                contar , caracter = 0 , tablero[i][j] 
                if caracter == "T":
                    for k in range(n-i):
                        filtrador = tablero[i+k][j]
                        if filtrador == "T" and k == 1:
                             contar += 1
                        else:
                             contar = contar
          
                    if contar == 1:
                        lista_tope.append(contar)
                    else: 
                        lista_tope.append(contar)
                pos += 1
    return lista_tope

#https://www.youtube.com/watch?v=W8PxekI2pk8  (copie el codigo del link adjuntado)
def suma_tope_tortugas(lista_tope: list):
    suma = []
    for j in range(len(lista_tope[0])):
         suma.append(0)
         

    for i in lista_tope:
         suma = list(map(lambda x , y : x + y , suma , i ))

    return suma


def sumar_lista_tortugas(tablero: str):
    lista=[]
    
    lista.append(contar_derecha_tortuga(tablero))
    lista.append(contar_izquierda_tortuga(tablero))
    lista.append(contar_arriba_tortuga(tablero))
    lista.append(contar_abajo_tortuga(tablero))

    return lista

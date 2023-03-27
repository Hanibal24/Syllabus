
#Retorna una lista con las bombas del tablero
def bombas (tablero:list):
    n , lista= len(tablero) , []
    for i in range(n):
            pos = 0
            for j in range(n):
                x = str(tablero[i][j])
                y = x.isdigit()
                if y == True:
                     lista.append(tablero[i][j])
    return lista

#Cuanta hasta donde alcanza la bomba 
# hacia la derecha antes de toparse con una tortuga o el final del tablero
def contar_derecha(tablero:list):
    n , lista_alcance = len(tablero) , []
    for i in range(n):
            pos = 0
            for j in range(n):
                alcance , llave , x = 0 , True , str(tablero[i][j])
                y = x.isdigit()
                if y == True:
                        for k in range (n-pos):
                            filtrador = tablero[i][pos+k]
                            if filtrador != "T" and llave == True:
                                    alcance += 1
                            elif filtrador == "T":
                                    llave = False
                        lista_alcance.append(alcance)
                pos+=1
    
    return lista_alcance


#Cuanta hasta donde alcanza la bomba hacia la 
# izquierda antes de toparse con una tortuga o el final del tablero
def contar_izquierda(tablero: list):
    n , lista_alcance = len(tablero) , []
    for i in range(n):
            pos = 0
            for j in range(n):
                alcance , llave , x = -1 , True , str(tablero[i][j])
                y = x.isdigit()
                if y == True:
                        for k in range (pos+1):
                            filtrador = tablero[i][pos-k]
                            if filtrador != "T" and llave == True:
                                    alcance += 1
                            elif filtrador == "T":
                                    llave = False
                        lista_alcance.append(alcance)
                pos+=1
    
    return lista_alcance


#Cuanta hasta donde alcanza la bomba hacia 
# la arriba antes de toparse con una tortuga o el final del tablero
def contar_arriba(tablero: list):
    n , lista_alcance = len(tablero) , []
    for i in range(n):
        for j in range(n):
            alcance , llave , x = -1 , True , str(tablero[i][j])
            y = x.isdigit()
            if y == True:
                for k in range (i+1): 
                    filtrador = tablero[i-k][j]
                    if filtrador != "T" and llave== True:
                        alcance += 1
                    elif filtrador == "T":
                        llave = False
                lista_alcance.append(alcance)
    

    return lista_alcance


#Cuanta hasta donde alcanza la bomba hacia la abajo 
#antes de toparse con una tortuga o el final del tablero
def contar_abajo(tablero: list):
    n , lista_alcance = len(tablero) , []
    for i in range(n):
        for j in range(n):
            alcance , llave , x = -1 , True , str(tablero[i][j])
            y = x.isdigit()
            if y == True:
                for k in range (n-i): 
                    filtrador = tablero[i+k][j]
                    if filtrador != "T" and llave== True:
                        alcance += 1
                    elif filtrador == "T" or filtrador == "─" :
                        llave = False
                lista_alcance.append(alcance)
    

    return lista_alcance




#https://www.youtube.com/watch?v=W8PxekI2pk8 
#(copie el codigo del link adjuntado) suma las listas con los alcances en todas la direcciones 
def suma_alcance(lista_alcance: list):
    suma = []
    for j in range(len(lista_alcance[0])):
         suma.append(0)
         

    for i in lista_alcance:
         suma = list(map(lambda x , y : x + y , suma , i ))

    return suma



#Crea una lista de listas  con los alcances en todas las direcciones, 
#lo retornado se usa en la funcion anterior (suma_alcance)             
def sumar_lista(tablero: str):
    lista=[]
    
    lista.append(contar_derecha(tablero))
    lista.append(contar_izquierda(tablero))
    lista.append(contar_arriba(tablero))
    lista.append(contar_abajo(tablero))

    return lista



#Contar al alcance antes de topar con una tortuga o el 
#final del tablero hacia abajo , de solo una bomba 
def contar_abajo_coordenada(tablero: list, coordenada: tuple):
    n=len(tablero)
    info_coordenada=str(tablero[coordenada[0]][coordenada[1]])
    y = info_coordenada.isdigit()
    llave = True
    a = coordenada[0]
    b = coordenada [1]
    if y == True:
        alcance=0
        for j in range(n-coordenada[0]):
            if tablero[a+j][b] != "T" and llave == True:
                alcance += 1
            elif tablero[a+j][b] == "T":
                 llave=False
    
        return alcance
    else:
        return 0
                   
#Contar al alcance antes de topar con una tortuga o 
# el final del tablero hacia arriba , de solo una bomba 
def contar_arriba_coordenada(tablero: list, coordenada: tuple):
    n=len(tablero)
    info_coordenada=str(tablero[coordenada[0]][coordenada[1]])
    y = info_coordenada.isdigit()
    llave = True
    a = coordenada[0]
    b = coordenada [1]
    alcance=-1
    if y == True:
        for j in range(coordenada[0]+1):
            if tablero[a-j][b] != "T" and llave == True:
                alcance += 1
            elif tablero[a-j][b] == "T":
                 llave=False
    
        return alcance
    else:
        return 0

#Contar al alcance antes de topar con una tortuga o el 
# final del tablero hacia la izquierda , de solo una bomba 
def contar_izquierda_coordenada(tablero: list, coordenada: tuple):
    n=len(tablero)
    info_coordenada=str(tablero[coordenada[0]][coordenada[1]])
    y = info_coordenada.isdigit()
    llave = True
    a = coordenada[0]
    b = coordenada [1]
    alcance=-1
    if y == True:
        for j in range(coordenada[1]+1):
            if tablero[a][b-j] != "T" and llave == True:
                alcance += 1
            elif tablero[a][b-j] == "T":
                 llave=False
    
        return alcance
    else:
        return 0
                   
#Contar al alcance antes de topar con una tortuga o el 
# final del tablero hacia la derecha , de solo una bomba 
def contar_derecha_coordenada(tablero: list, coordenada: tuple):
    n=len(tablero)
    info_coordenada=str(tablero[coordenada[0]][coordenada[1]])
    y = info_coordenada.isdigit()
    llave = True
    a = coordenada[0]
    b = coordenada [1]
    alcance=-1
    if y == True:
        for j in range(n-coordenada[1]):
            if tablero[a][b+j] != "T" and llave == True:
                alcance += 1
            elif tablero[a][b+j] == "T":
                 llave=False
    
        return alcance
    else:
        return 0
                   
    
     

from contar_bombas import contar_derecha , contar_abajo , contar_arriba , contar_izquierda , suma_alcance , bombas , sumar_lista , contar_abajo_coordenada , contar_arriba_coordenada , contar_izquierda_coordenada , contar_derecha_coordenada
from tablero import imprimir_tablero

#Todas las soluciones posible de la bomba, usando solo la fila hacia la derecha 
def solucion_derecha(tablero: list , coordenada: tuple):
    fila=tablero[coordenada[0]]
    n=len(tablero)
    llave =False
    lista=[]
    for i in range(n-coordenada[1]-1):
        lista.append(str(tablero)) #Agregamos el tablero en forma de string para que 
                                   #no cambie con las propiedades de lista que usaremos mas 
                                   #adelnate (al intertar guardalo de otra forma, la lista cambiaba sin parar)

        if llave == True:

            fila.insert(-i,og)
            fila.pop(-i)
            tablero.insert(coordenada[0], fila)
            tablero.pop(coordenada[0])
        
        og=tablero[coordenada[0]][-i-1] #guarda el caracter o coordenada inicial, 
                                        #el cual usaremos para obtener nuestra fila original 
        
        fila.insert(-i-1,"T")
        fila.pop(-i-1)
        tablero.insert(coordenada[0], fila)
        tablero.pop(coordenada[0])
        llave=True
    
    for i in range(coordenada[0]):
        lista.append(str(tablero))
    return lista  



#todas las posible soluciones de la bomba, usando solo la fila hacia la izquierda 
#(usamos los mismo valoreds de solucion_izquierda, cambiamos la direcccion en la 
# cual se guardan los caracteres y la cantidad de veces que itera)
def solucion_izquierda(tablero: list , coordenada: tuple):
    n=len(tablero)
    fila=tablero[coordenada[0]]
    llave_1 =False
    lista=[]
    for i in range(coordenada[1]+1):
        lista.append(str(tablero))

        if llave_1 == True:

            fila.insert(i-1,og)
            fila.pop(i)
            tablero.insert(coordenada[0], fila)
            tablero.pop(coordenada[0])
            
        
        og=tablero[coordenada[0]][i]
        llave_1=True
    
        fila.insert(i,"T")
        fila.pop(i+1)
        tablero.insert(coordenada[0], fila)
        tablero.pop(coordenada[0])
        
    for i in range(n-coordenada[0]):
        lista.append(str(tablero))

    return lista  

#Todas las posibles soluciones de la bomba solo usando la columna de arriba 
def solucion_arriba(tablero: list , coordenada: tuple):
    n=len(tablero)

    lista=[]
    llave_1= False
    for i in range(coordenada[0]+1):
        lista.append(str(tablero))

        if llave_1 == True:

            tablero[i-1].insert(coordenada[1],og)
            tablero[i-1].pop(coordenada[1]+1)
        
            
        
        og=tablero[i][coordenada[1]]
        llave_1=True
    
        tablero[i].insert(coordenada[1],"T")
        tablero[i].pop(coordenada[1]+1)
    

    for i in range(n-coordenada[0]):
        lista.append(str(tablero))
    return lista
    

#Todas las posibles soluciones de la bomba solo usando la columna de abajo 
def solucion_abajo(tablero: list , coordenada: tuple):
    n=len(tablero)
    a=n-1
    

    lista=[]
    llave_1= False
    for i in range(n-coordenada[0]):
        lista.append(str(tablero))
        
        if llave_1 == True:

            tablero[a-i+1].insert(coordenada[1],og)
            tablero[a-i+1].pop(coordenada[1]+1)
        
        og=tablero[a-i][coordenada[1]]
        llave_1=True
    
        tablero[a-i].insert(coordenada[1],"T")
        tablero[a-i].pop(coordenada[1]+1)
    
    for i in range(coordenada[0]):
        lista.append(str(tablero))

    return lista

   


 

#Utiliza la lista de cualquiera de las soluciones_derecha,izquierda,arriba,abajo 
#para crear un str sin los [] y luego crear otra lista (las soluciones entregan [] 
# equivalentes a caracteres, hay que eliminarlos)
def split_lista(tablero: list):
    str=""
    for caracter in tablero:
        for caracter2 in caracter:

            x=caracter2.isdigit()
            if x == True or caracter2 == "T" or caracter2 == "-":
                str += caracter2 + ","
    lista=str.split(",")
    lista.pop(len(lista)-1)
    
    return lista
            
#resive la lista de split_lista y crea una lista de listas con 
# cada tablero que equivale a la solucion de una bomba 
def armando_lista(tablero: list, lista: list):
    n=len(tablero)
    lista_pueba=[]
    tablero_3=[]
    for k in range(n):
        tablero_2=[]
        lista_pueba.append([])
        for j in range (n):
            tablero_1=[]
            for i in range(n):
                if lista != []:
                    tablero_1.append(lista[0])
                    lista.pop(0)
                else:
                    pass
            tablero_2.append(tablero_1)
        tablero_3.append(tablero_2)
    
    for i in range(len(tablero_3)):
        if tablero_3[-1] == lista_pueba:
            tablero_3.pop(-1)

    return tablero_3


#Guarda la cordenada de la bomba 
def guardar_coordenada(tablero:list):
    lista_coordenadas=[]
    for i in range (len(tablero)):
        for j in range(len(tablero)):
            x=str(tablero[i][j])
            y=x.isdigit()
            if y ==True:
                coordenada=(i,j)
                lista_coordenadas.append(coordenada)
    
    return lista_coordenadas






#Deria de combinar todas las soluciones de una bomba para luego solartar las nuevas soluciones combinadas , 
def sol_tablero_bomba(tablero: list):
    coordenadas=guardar_coordenada(tablero)
    
        


        
    pass




    

    

        


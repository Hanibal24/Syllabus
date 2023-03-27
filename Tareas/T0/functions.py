# Agregar los imports que estimen necesarios
from tablero import imprimir_tablero
from contar_bombas import contar_derecha , contar_abajo , contar_arriba , contar_izquierda , suma_alcance , bombas , sumar_lista , contar_abajo_coordenada , contar_arriba_coordenada , contar_izquierda_coordenada , contar_derecha_coordenada
from contar_tortugas import contar_derecha_tortuga , contar_izquierda_tortuga , contar_arriba_tortuga , contar_abajo_tortuga , suma_tope_tortugas , sumar_lista_tortugas , tortugas
from soluciones_tablero import solucion_derecha , solucion_izquierda , split_lista , armando_lista , solucion_arriba , solucion_abajo , sol_tablero_bomba , guardar_coordenada


def cargar_tablero(nombre_archivo: str) -> list:

    with open(nombre_archivo,"r") as f:
        texto=f.read()
        n=int(texto[0])
        texto=texto[2:len(texto):2]
    
    tablero=[]

    while len(texto)!=0:
        lista_1=[]
        for i in range(n):
            lista_1.append(texto[i])
        
        texto=texto[n:len(texto)+1]    
        tablero.append(lista_1)
    
    return tablero


def guardar_tablero(nombre_archivo: str, tablero: list) -> None:

    pass


def verificar_valor_bombas(tablero: list) -> int:
    lista=sumar_lista(tablero) 
    lista_bombas= bombas(tablero)
    bombas_invalidas = 0

    lista_suma = suma_alcance(lista)

    for i in range (len(lista_suma)):
        if str(lista_suma[i]) != lista_bombas[i]:
            bombas_invalidas += 1
        else:
            bombas_invalidas=bombas_invalidas
    
    return bombas_invalidas
    

def verificar_alcance_bomba(tablero: list, coordenada: tuple) -> int:
    a=contar_derecha_coordenada(tablero, coordenada)
    b=contar_izquierda_coordenada(tablero, coordenada)
    c=contar_arriba_coordenada(tablero, coordenada)
    d=contar_abajo_coordenada(tablero, coordenada)
    

    

    return a+b+c+d



def verificar_tortugas(tablero: list) -> int:
    lista=sumar_lista_tortugas(tablero) 
    tortugas_invalidas = 0

    lista_suma = suma_tope_tortugas(lista)

    for i in range (len(lista_suma)):
        if lista_suma[i]>= 1:
            tortugas_invalidas += 1
        else:
            tortugas_invalidas=tortugas_invalidas
    
    return tortugas_invalidas






def solucionar_tablero(tablero: list) -> list:
    lista_coordenadas=guardar_coordenada(tablero)









    pass


if __name__ == "__main__":
    tablero_2x2 = [
        ['-', 2],
        ['-', '-']
    ]
    resultado = verificar_valor_bombas(tablero_2x2)
    print(resultado)  # Debería ser 0

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 3

    tablero_resuelto = solucionar_tablero(tablero_2x2)
    print(tablero_resuelto)

    tablero_2x2_sol = [
        ['T', 2],
        ['-', '-']
    ]

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 2

    resultado = verificar_tortugas(tablero_2x2_sol)
    print(resultado)  # Debería ser 0

tablero = cargar_tablero("Archivos\\4x4_sol.txt")
tablero_1 = cargar_tablero("Archivos\\5x5.txt")
print(imprimir_tablero(tablero_1))
#print(solucion_derecha(tablero_1,(4,4)))
a=solucion_derecha(tablero_1,(3,3))
b=split_lista(a)
c=armando_lista(tablero_1,b)

for i in range(len(c)):

    print(c[i])

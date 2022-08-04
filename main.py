'''
TO DO: 
    - Crear una variable  que tenga la cantidad de barras bajas según el tamaño de la palabra oculta. ✅

    - Comprobar si la letra introducida se encuentra en la palabra oculta y mostrarlo en pantalla. ✅
    
    - Chequear si hay redundancia en 'barras' y 'barras_bajas'.

    - Incluir todo el programa en un bucle y que se termine despues de 6 intentos fallidos o si se adivina la palabra.

'''
import random
from functools import reduce

def main(): 
    # Guardamos las palabras a adivinar en una lista
    with open('./archivos/words.txt', 'r', encoding='utf-8') as f:
        palabras = [word for word in f]

    # Seleccionamos una palabra aleatoria de la lista de palabras con random.choice
    palabra_oculta = random.choice(palabras)
    
    # Eliminamos los errores de caracteres en la lista con '.replace'
    palabra_oculta = palabra_oculta.replace('\n','')
    
    # Creamos una variable con la misma cantidad de '_' que letras en palabra_oculta
    barras = len(palabra_oculta) * '_'
    
    # Tranformamos barras en una lista con cada caracter 
    barras_bajas = [char for char in barras]
    
    # Tranformamos la palabra oculta en una lista con cada caracter de la palabra
    caracteres = [letra for letra in palabra_oculta]

    print(palabra_oculta)

    print('Bienvenido al juego del ahorcado')
    
    vidas = 5

    while vidas > 0:
        
        print(barras_bajas)
        intento = input('Con que letra queres probar?: ')

    
        indice = 0
        for letra in caracteres:
            if letra == intento:
                barras_bajas[indice] = intento
            indice = indice + 1

        if barras_bajas == caracteres:
            print('Ganaste!, la palabra era ' + palabra_oculta)
            

    '''if intento == palabra_oculta:
       print('Ganaste')
    else:
        print('Perdiste')'''




if __name__ == '__main__':
    main()
    
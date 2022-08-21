

def diccionar(palabra):
    posicion = 0
    po_dict = {}
    
    for letra in palabra:
        posicion = posicion + 1
        po_dict[posicion] = letra
    
    #Retorna un diccionario con cada letra de la palabra y su posicion
    return po_dict 

def main():

    palabra_oculta = 'zapatila'
    
    barras = len(palabra_oculta) * '_'
    
    intento = 'z'

    palabra_oculta_preparada = dict(enumerate(palabra_oculta,1))
    
    print(palabra_oculta_preparada)
   # print(palabra_oculta_preparada.get('z'))


if __name__ == '__main__':
    main()
    
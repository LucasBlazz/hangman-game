# Tratando de reemplazar el intento en barras bajas
intento = 'z'
palabra = 'zapatilla'
barras_bajas = ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ']

caracteres = [i for i in palabra]
indice = 0

for letra in caracteres:
    if letra == intento:
        barras_bajas[indice] = intento
    indice = indice + 1

        
        
    

print(caracteres)
print(barras_bajas)




'''for letra in palabra:
    
    if letra == intento:
        barras_bajas = barras_bajas.replace(letra,intento)
        print(barras_bajas)'''


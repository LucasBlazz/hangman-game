# Tratando de reemplazar el intento en barras bajas
intento = 'a'
palabra_oculta = 'zapatilla'
barras_bajas = ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ']

caracteres = [i for i in palabra_oculta]
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


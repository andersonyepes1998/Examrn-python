
numeros =[(50,45,20,30,40,87)]

print(numeros)

conjunto = set().union(*numeros)
print(conjunto)

resultado = sorted(conjunto)
print(resultado)

#--------------------------------

tuplas = (50,45,20,30,40,87)

listas = list(tuplas)
for lista in listas:
    if lista>40:
        print(lista)

#--------------------------------


tuplas2 = (50,45,20,30,40,87)

numerolistas = list(tuplas2)
for i in numerolistas:
    if i/2:
        print(i)


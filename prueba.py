
""" Numeros Primos del 1 al 100 

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 , 97

"""

cant_primos = 0

def nro_primo(nro):
    divisores=0
    for indice in range(1, nro+1):
        if nro % indice == 0:
            divisores+=1

    if divisores==2:
        print(nro)
        global cant_primos
        cant_primos+=1
       

for nro in range(1, 101):
    nro_primo(nro)


print(str(cant_primos) + " son primos")



## metodo de la secante 
import numpy as np

fxs = lambda x: x**3 - 2*x -5
b = 1.9
a = 2
error = 0.009

def secante(a,b,error):
    ep= 0
    tabla = []
    while (ep>=error or ep == 0):
        fa = fxs(a)
        fb = fxs(b)
        c = a - (fa*(b-a))/(fb-fa)
        ep = abs((c-b)/c)*100
                
        tabla.append([b,a,fa,fb,c,ep])
        b = a
        a = c
    return(tabla)

#Ejecucion del metodo de la secante
tabla = secante(a,b,error)
n = len(tabla)
raiz = tabla[len(tabla)-1][4]

#Salida del metodo secante
print('[xa ,\t xb , \t xc , \t ep]')
for i in range(0,n,1):
    print(tabla[i])
print('raiz en: ', raiz)
import numpy as np

fx = lambda x: x**3 + 4*(x**2) - 10

a = 1 
b = 2

error = 0.0001

#Metodo de regula falsi
def regulaFalsi(a,b,fx,error):
    tabla = []
    intervalo = abs(b-a)
    fa=fx(a)
    fb=fx(b)

    while not (intervalo <= error):
        c = b - ((fb*(a-b))/(fa-fb))

        fc=fx(c)

        tabla.append([a,c,b,fa,fc,fb,intervalo])
        cambios = np.sign(fa)*np.sign(fc)

        if cambios>0:
            intervalo=abs(c-a)

            a = c 
            fa = fc
        else:
            intervalo=abs(b-c)
            b = c
            fb = fc
    return(tabla)

tabla = np.array(tabla)
ntabla = len(tabla)


#Salida del metodo regula falsi 
np.set_printoptions(precision=3)
for i in range(0,ntabla,1):
    print('iteracion', i)
    print('[a,c,b]:    ', tabla[i,0:3])
    print('[fa,fc,fb]: ', tabla[i,3:6])
    print('[tramo]:    ', tabla[i,6])

print('raiz:  ',c)
print('error: ',error)



## metodo de la secante 
def secante(fx,xa,error):
    dx = 4*error        
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=error):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = abs(xc-xa)
                
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

        tabla = np.array(tabla)
        
        return(tabla)

#Ejecucion del metodo de la secante
tabla = secante(fx,xa,error)
n = len(tabla)
raiz = tabla[n-1,2]

#Salida del metodo secante
np.set_printoptions(precision=4)
print('[xa ,\t xb , \t xc , \t tramo]')
for i in range(0,n,1):
    print(tabla[i])
print('raiz en: ', raiz)



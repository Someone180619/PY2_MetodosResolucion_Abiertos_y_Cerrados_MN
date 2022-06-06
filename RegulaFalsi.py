import numpy as np

fxrf = lambda x: -0.5*x**2 + 2.5*x + 4.5

a = -2
b = 1
error = 0.008

#Metodo de regula falsi
def regulaFalsi(a,b,fx,error):
    tabla = []
    ep = 0
    fa=fx(a)
    fb=fx(b)
    while (ep >= error or ep == 0):
        c = b - ((fb*(a-b))/(fa-fb))

        fc=fx(c)

        tabla.append([a,c,b,fa,fc,fb,ep])
        cambios = np.sign(fa)*np.sign(fc)
        if cambios>0:
            ep=abs((c-a)/a)*100
            a = c 
            fa = fc
        else:
            ep=abs((c-b)/b)*100
            b = c
            fb = fc
    return(tabla)

tabla = regulaFalsi(a, b, fxrf, error)
ntabla = len(tabla)

#Salida del metodo regula falsi 
for i in range(0,ntabla,1):
    print('iteracion', i)
    print('[a,c,b,fa,fc,fb,ep]:    ', tabla[i])

print('raiz:  ',tabla[len(tabla)-1][2])
print('error: ',error)
import numpy as np
from sympy import *
from tabulate import tabulate

a = 0
b = 0
error = 0

# Metodo de regula falsi
def regulaFalsi(a, b, ent, error):
    x = Symbol("x")
    fxrf = lambda x: eval(ent)
    tabla = []
    ep = 0
    i=0
    fa = fxrf(a)
    fb = fxrf(b)
    while (ep >= error or ep == 0):
        c = b - ((fb*(a-b))/(fa-fb))
        fc = fxrf(c)
        try:
            tabla.append([i, a, c, b, fa, fc, fb, ep])
            cambios = np.sign(fa)*np.sign(fc)
            if cambios > 0:
                ep = abs((c-a)/a)*100
                a = c
                fa = fc
            else:
                ep = abs((c-b)/b)*100
                b = c
                fb = fc
            assert a or b ==0 
        except ZeroDivisionError:
            break

        i+=1    
    return(tabla)

# Método Secante
def secante(a, b,ent, error):
    x = Symbol("x")
    fxs = lambda x: eval(ent)
    ep = 0
    i=0
    tabla = []
    while (ep >= error or ep == 0):
        fa = fxs(a)
        fb = fxs(b)
        c = a - (fa*(b-a))/(fb-fa)
        ep = abs((c-b)/c)*100

        tabla.append([i, b, a, fa, fb, c, ep])
        b = a
        a = c
        i+=1
    return(tabla)


# Menú
continuar = True
while continuar:
    try:
        print("""

        Proyecto 2 - Métodos de resolución
                [1]Presentación
                [2]Método cerrado: Regula Falsi
                [3]Método abierto: Secante
                """)
        opt = int(input("Seleccione una opción: "))

        if(opt < 1 or opt > 3):
            print("opcion equivocada, favor validar")
        else:

            if opt>1:
                ent = input("Ingrese la funcion: ")
                print("Ingrese el intervalo a evaluar:")
                a = float(input("a: "))
                b = float(input("b: "))
                error = float(input("error: "))

            if opt == 1:
                print("""
                    Desarrollado por:
                        Cortez, Brandool
                        Estribí, Fernando

                    Grupo: 1SF131""")
            elif opt == 2:
                tabla = regulaFalsi(a, b, ent, error)
                ntabla = len(tabla)

                # Salida del metodo regula falsi
                header = ['i', 'a', 'c', 'b', 'fa', 'fc', 'fb', 'ep']
                print(tabulate(tabla, headers=header, floatfmt=".4f"))

                print('raiz:  ', "{:.4f}".format(tabla[len(tabla)-1][2]))
                print('error: ', "{:.4f}".format(tabla[ len(tabla)-1][6]))
            elif opt == 3:
                tabla = secante(a, b,ent, error)
                n = len(tabla)
                raiz = "{:.4f}".format(tabla[len(tabla)-1][5])

                # Salida del metodo secante
                header = ['i', 'b', 'a', 'fa', 'fb', 'xc', 'ep']
                print(tabulate(tabla, headers=header, floatfmt=".4f"))
                print('raiz en: ', raiz)
                print('error: ', "{:.4f}".format(tabla[ len(tabla)-1][6]))
           
    except ValueError:
        print("Dato ingresado no numérico. Intente de nuevo.")

    answer = None
    while answer not in ("y", "n"):
        answer = input("¿Desea realizar otro procedimiento? [y/n]: ")
        if answer == "y":
            pass
        elif answer == "n":
            continuar = False
        else:
            print("Opcion invalida. Intente de nuevo.")

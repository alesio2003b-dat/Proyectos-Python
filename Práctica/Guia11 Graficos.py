#Graficos
import matplotlib.pyplot as plt

#Ejercicio 1
#Primer ejercicio, gráfico simple
x=[0,1,2,3,4]
y=[2,4,1,5,3]
# plt.plot(x,y)
# plt.show()

#Ejercicio 2
#Graficar funcion
def graficarfuncion(f,x0,xf,dx):
    import numpy as np
    x=np.arange(x0,xf,dx)
    print(x)
    y=[f(i) for i in x]
    print(y)
    plt.plot(x,y)
    return plt.show()
# print(graficarfuncion(lambda x: x**2, 0,5,0.1))

#Ejercicio 3
# Grafica circulo
def Circulo (r,x0,y0):
    import math
    import numpy as np
    tita= np.arange(0,2*math.pi,0.01)
    x=[r*math.cos(i) + x0 for i in tita]
    y=[r*math.sin(i) + y0 for i in tita]
    plt.plot(x,y)
    return plt.show()
# print(Circulo(3,2,1))

#Ejercicio 4
#Tiro parabólico
def tiro(v0,alpha,y0=0):
    import math
    import numpy as np
    t=np.arange(0,50,0.00001)
    g=9.81
    
    x=[v0*math.cos(alpha)*i for i in t]
    y=[y0 + v0*math.sin(alpha)*i - 0.5*g*i**2 for i in t]
    a=0
    for i in y:
        if i<0:
            break
        a=a+1
    x=x[:a]
    y=y[:a]
    plt.plot(x,y)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Altura")
    plt.title("Altura vs tiempo")
    return plt.show()
# print(tiro(5,1.47))

#Ejercicio 5 (Este creo que no me salió como debería salir, mejor dicho, a chat gpt)
#Triangulo
def graficar_triangulo(b, h):
    # Coordenadas de los vértices del triángulo
    x = [0, b / 2, -b / 2, 0]
    y = [0, h, h, 0]
    
    # Graficar el triángulo
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'b-')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Triángulo Isósceles')
    plt.grid(True)
    plt.axis('equal')
    return plt.show()
# print(graficar_triangulo(10,5))

#Ejercicio 6 
#Cinética
def primerorden(A0,k):
    import math
    import numpy as np
    t=np.arange(0,30,0.1)
    A=[A0*math.e**(-k*i) for i in t]
    a=0
    for i in A:
        if i<0.01:
            break
        a=a+1
    t=t[:a]
    b=A[:a]
    plt.plot(t,b)
    return plt.show()
# print(primerorden(4,0.35))

#Ejercicio 7
#Parte 2 del de cinetica
def borden(A0,B0,k):
    import math
    import numpy as np
    t=np.arange(0,30,0.1)
    B=[B0+A0*(1-math.e**(-k*i)) for i in t]
    A=[A0*math.e**(-k*i) for i in t]
    g=0
    for i in A:
        if i<0:
            break
        g=g+1
    t=t[:g]
    a=A[:g]
    b=B[:g]
    plt.figure(figsize=(8, 6))
# Graficar la primera función
    plt.plot(t, a, label='Concentracion de A', color='blue')
# Graficar la segunda función sobre la misma figura
    plt.plot(t, b, label='Concentración de B', color='red')
    plt.legend()
    return plt.show()
# print(borden(30,0,0.35))    

#Ejercicio 8
#Ecocardiograma
def ecocardiograma(nombre):
    t=[]
    ec=[]
    with open(nombre, "r") as algo:
        for i in algo:
            a=i.strip().split(",")
            print(a)
            t.append(float(a[0]))
            ec.append(float(a[-1]))
        plt.plot(t,ec)
    return plt.show()
# print(ecocardiograma("ecg.csv.txt"))

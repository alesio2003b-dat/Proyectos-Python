#Ejercicio 1
#Sumar
#def Sumarhasta(n):
#    if n>0:
#        a=0
#        for i in range(n+1):
#            a=a+i
#    if n<=0:    
#        return None
#    return a

#print(Sumarhasta(5))

###########################################
#Ejercicio 2
#def afahrenheit(cel):
#    fah=(cel*9/5)+32
#    return fah
#print(afahrenheit(300))

#Ejercicio 3
#Angulo en grados minutos y segundos a radianes:
#import math
#def angrad(grados,minutos,segundos):
#    rad= (grados+(minutos+segundos/60)/60)*math.pi/180
#    return(rad)
#print(angrad(20,50,10))

#Ejercicio 4
#Horas minutos segundos
#def horas(segundos):
#    minuto= segundos/60
#    horas= int(minuto //60)
#    tiempo= round(minuto-horas*60)
#    segundo= segundos//60
#    real= round(segundos- segundo*60)
   
#    print(segundos, "segundos son: ", horas, "horas,  ", tiempo, "minutos y",real, "Segundos")
#print(horas(8546))

#################
#Ejercicio 5
#Funcion
#def signo(x):
#    if x>0:
#        a=1
#    elif x<0:
#        a=-1
#    else:
#        a=0
#    return a
#print(signo(5))
#print(signo(-5))
#print(signo(0))

#Ejercicio 6
#def habermundial(a):
#    M= "No hubo mundial"
#    N= "Hubo Mundial"
#    H= "Habrá un munidial ese año"
#    b=[ 0]
#    Mundial=True
#    if a<1930:
#        return M
#    for i in range(1930,4000,4):
#         b.append(i)
#    b.remove(0)
#    for i in range(0,len(b)):
#        if int(a/b[i]) !=1:
#            Mundial=True
#        elif int(a/b[i])==1 and a<2023 and a>1930:
#            return N
#            Mundial=False
#            break
#        elif int(a/b[i])==1 and a>2023 :
#            Mundial=False
#            return H
#            break
#    if Mundial==True:
#        return M
#print(habermundial(2026))

##################################
#Ejercicio 7
#Factorial
def factorial(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
# print(factorial(5))

#Ejercicio 8 y Ejercicio 30
#Discriminante
# def discriminante(a,b,c):
#     d=b**2-4*a*c
#     return d
# def tipos(a,b,c):
#     if discriminante(a,b,c)>0:
#         e="Raices Reales y distintas"
#         return e
#     elif discriminante(a,b,c)== 0:
#         f="Raices Reales e iguales"
#         return f
#     else:
#         i="Raices complejas conjugadas"
#         return i
# print(tipos(1,4,4))

#El de mcm no lo hice creo
# def mcm(a,b):
#     c=True
#     i=0
#     while c==True:
#         i=i+1
#         if i%a==0 and i%b==0:
#             c=False
#     return i
# print(mcm(76,97))

#Ejercicio 10
def extension(palabra):
    a=0
    for i in range(len(palabra)):
        if palabra[i]==".":
            a=i
    return palabra[a+1:]
# print(extension("hola.txt"))

#Ejercicio 12
def div(n1,n2=True):
    if n2==True:
        return n1
    else:
        return n1/n2

#Ejercicio 13
def pot(n1,n2=True):
    if n2==True:
        return n1
    else:
        return n1**n2
#Ejercicio 14
def descuento(precio,desc=True):
    if desc==True:
        precio=precio-precio*0.1
    else:
        precio=precio-precio*desc/100
    return precio
# print(descuento(100,20))

#Ejercicio 15
#Rectangulo
#def rectangulo(a,b,c=True):
#    d=("*" * b)
#    if c==True:
#        return a*b
#    else:
#        for i in range(a):
#           return c*b
#print(rectangulo(2,4,5))

########################################
#Ejercicio 17
#Hola Nombres
#def nombres(*nom):
#    for i in (nom):
#        print("¡Hola",i,"!") 
#print(nombres("Alesio", "Maddi"))

#########################################
#Ejercicio 18
#Letra cadena
#def letradena(letra,*cadenas):
#    aparicion=0
#    for let in cadenas:
#        for tre in range(len(let)):
#            if letra==let[tre]:
#                aparicion= aparicion+1
#    return aparicion
#print(letradena("a", "computadora", "mate amargo", "botella" ))

#################################################
#Ejercicio 19
#Producto total
#def producto(*n):
#    a=1
#    for i in range(len(n)):
#        a=a*n[i]
#    return a
#print(producto(4,5,2,3,4))

#######################################################
#Ejercicio 20
#Concatenar enterros
#def conc(*n):
#    a=" "
#    for i in range(len(n)):
#        a=a+str(n[i])
#    return a
#print(conc(1,2,3,4))

########################################################
#Ejercicio 21
#Concatenar palabras
#def pal(*palabras, sep=" "):
#    a= ""
#    for i in palabras:
#        if i != palabras[-1]:
#            a=a+i+sep
#        if i == palabras[-1]:
#            a=a+i 
#    return a
#print(pal("Esto", "es", "una", "prueba", sep="-"))

#################################
#Ejercicio 23
#def division(dividendo, divisor):
#    """Asume dividendo y divisor enteros o flontantes,
#    divisor distinto de 0.
#    Devuelve flotante dividendo / divisor.
#    Si divisor == 0, devuelve None e imprime
#    un mensaje."""
#    if divisor == 0:
#        print('divisor debe ser distinto de 0')
#        return None
#    return dividendo / divisor
#help(division)

##################################
#Ejercicio 24
#def repetidor(mensaje , c):
#    """Asume mensaje string y c entero.
#    Devuelve string mensaje_repetido,
#    repetición de mensaje separado por espacios,
#    rep etido c veces.
#    Si c==0, devuelve ''."""
#    if c==0:
#        a= "."
#        return a
#    b= (str(mensaje) + " ")* c
#    return b
#print(repetidor( "hola", c=2))
########################################

#Ejercicio 25

#def f1(x):
#    y=x**2
#    return y
#def f2(x):
#    z=x-1
#    return z
#def diferencia_funciones(x, f1, f2):
#    """Asume x flotante o entero, f1 y f2 funciones.
#   Devuelve entero o flotante dif_f,
#  diferencia absoluta entre f1(x) y f2(x)."""
#    return f1(x)-f2(x)
#print(diferencia_funciones(5,f1,f2))

#No les agregué las especificaciones en su momento y tampoco lo voy a hacer ahora. Les toca a ustedes.
##########################################
#Ejercicio 27
# def biseccion(f, poco, mucho):
#     eps = 1.0e-7
#     fpoco = f(poco)
#     fmucho = f(mucho)
#     while True:
#         medio = (poco + mucho) / 2
#         fmedio = f(medio)
#         #print(medio, fmedio)
#         if abs(fmedio) < eps:
#             break
#         if fmedio < 0:
#             poco = medio
#         else:
#             mucho = medio
#     return medio
# def f(x):
#     return x**3- 2*x**2-3*x+2

# print(biseccion(lambda x: x**2 - 1, -1, 2))
# print(f(-1.3429))

#########################################
#Ejercicio 28
# suma=lambda a,b: a+b
# resta=lambda a,b: a-b
# multiplicacion=lambda a,b: a*b
# division=lambda a,b: a/b
# potencia=lambda a,b: a**b

#Ejercicio 30
# def calculadora(operacion,a,b):
#     a=float(input("Ingrese un número: "))
#     b=float(input("Ingrese un npumero: "))
#     return operacion(a,b)
# print(calculadora(suma,4,5))
########################################
#El ejercicio 30 está mas arriba junto con el ejercicio del discriminante

##########################################
#Ejercicio 31
# def signo(x):
#     if x>0:
#         return 1
#     if x<0:
#         return -1
#     if x==0:
#         return 0

# f_esp=lambda x: x**4 *signo(x)
# print(f_esp(0))

#No hice el del MCD
# def mcd(a,b):
#     c=1
#     d=True
#     while d==True:
#         c=c+1
#         if c%a==0 and c%b==0:
#             d=False     
#     Mcd= a*b/c
#     return Mcd, c
# print(mcd(18,6))
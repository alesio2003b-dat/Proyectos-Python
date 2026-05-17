##Ejercicio 1
##i=1
##while i<6:
##    n=int(input("Ingrese un número entero: "))
##    if n%2==0:
##        print("Su numero es par")
##    else:
##        print("Su numero es impar")
##    i=i+1
##
##--------------------------------------------------------------------------------
##Ejercicio 2
##i=1
##while i<20:
##    print(i)
##    i=i+2
##------------------------------------------------------------------------------
##Ejercicio 3
##i=0
##while i<100:
##    print(i)
##    i=i+7
##---------------------------------------------------------------------------------
##Ejercicio 4
##n=int(input("Ingrese un número entero: "))
##factorial=1
##i=1
##while i<=n:
##    factorial=factorial*i
##    i= i+1
##print(factorial)
##--------------------------------------------------------------------------------
##Ejercicio 5:
##n=int(input("Ingrese un número entero: "))
##d=n/10
##i=1
##while d>=1:
##    i=i+1
##    d=d/10
##print(i)
##--------------------------------------------------------------------------------
##Ejercicio 6
##n=float(input("Ingrese un número decimal: "))
##no=float(-1)
##suma=0
##i=0
##while n!=no:
##    suma=suma+n
##    i=i+1
##    n=float(input("Ingrese un número decimal: "))
##print(suma, "Y", i)
##--------------------------------------------------------------------------------
##
##Ejercicio 7
##n=input("Ingrese un número entero: ")
##i=0
##impar=0
##cantidad= len(n)
##while i<cantidad:
##    if int(n[i])%2!=0:
##        impar=impar+1
##    i=i+1
##print(impar)
##--------------------------------------------------------------------------------
##Ejercicio 8
##cadena=input("Ingrese una palabra: ")
##valor= int(input("Ingrese la cantidad de veces que quiere que la palabra se repita: "))
##i=1
##while i<5:
##    print(cadena * valor)
##    cadena=input("Ingrese una palabra: ")
##    valor= int(input("Ingrese la cantidad de veces que quiere que la palabra se repita: "))
##    i=i+1
##--------------------------------------------------------------------------------
##Ejercicio 9
##import math
##n= float(input("Ingrese un número entre 0 y 10, estos inclusives"))
##while 0>n or n>10:
##     n= float(input("Ingrese un número entre 0 y 10, estos inclusives"))
##print(math.sin(n))
##--------------------------------------------------------------------------------
##Ejercicio 10:
##cadena= input("Ingrese una palabra: ")
##letra= input("Ingrese una letra contenida en la palabra: ")
##cantidad= len(cadena)
##i=0
##while i<cantidad:
##    if cadena[i]==letra:
##        print("La letra", letra, "Se encuentre en la poscición:",i)
##    i=i+1
##--------------------------------------------------------------------------------
##Ejercicio 11/12
##cadena=input("Ingrese una palabra: ")
##fin= str("FIN")
##i=0
##largo=0
##corto=9999999
##while cadena!=fin:
##    letra=input("Ingrese una letra: ")
##    if cadena[0]==letra:
##        i=i+1
##    if largo<len(cadena):
##        largo=len(cadena)
##        larga=cadena
##    if corto>len(cadena):
##        corto=len(cadena)
##        corta=cadena
##    cadena=input("Ingrese una palabra: ")
##print("La cantidad de cadenas ingresadas por el usuario que comienzan con la misma letra son: ",i)
##print("La palabra más larga es: ",larga, "y la cadena más corta es: ", corta)
##--------------------------------------------------------------------------------

##---------------------------------------------------------------------------------
##Ejercicio 13
##primero=int(input('Ingrese un valor entero: '))
##contador=1
##menor=99999999 #inicializo variable en un valor muy grande para forzar
##            # a que la 1er diferncia sea menor al de la variable menor
##lista=[] #inicializo variable con lista vacía
##
##while contador<4:
##    valor=int(input('Ingrese otro valor entero: '))
##    diferencia=abs(primero-valor)
##
##    if diferencia<menor:
##        menor=diferencia
##        lista=[valor] #guardo el número mas cercano a primero
##
##    elif diferencia==menor:#cuando tengo dos distancias/diferencia iguales 
##        lista.append(valor)#agrego a lista la nueva diferencia
##
##    contador=contador+1
##
##print('El/los número/s más cercano/s a',primero,'es/son:',lista)     
##--------------------------------------------------------------------------------

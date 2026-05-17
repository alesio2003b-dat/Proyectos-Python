##def area(base,altura):
##    """Funcicon que calcula el área de un triangulo"""
##    base=float(input("Ingrese la base de su triangulo: "))
##    altura=float(input("Ingrese la altura de su triangulo: "))
##    print("El área de su triangulo es: ", (base*altura)/2)
##area()

##n=input("Ingrese una palabra: ")
##l=input("Ingrese una letra: ")
##i=0
##while i<=len(n):
##    if n[i]==l:
##        print("La letra: ",l,"se encuentra en la posición: ",i)
##    i=i+1

##n=input("Ingrese una palabra: ")
##vocal=0
##for i in n:
##    if i=="a":
##        vocal=vocal+1
##    if i=="e":
##        vocal=vocal+1
##    if i=="i":
##        vocal=vocal+1
##    if i=="o":
##        vocal=vocal+1
##    if i=="u":
##        vocal=vocal+1
##print("Su palabra tiene ",vocal,"vocales")

##n=int(input("Ingrese un número: "))
##i=1
##factorial=1
##while i<=n:
##    factorial=factorial*i
##    i=i+1
##print(factorial)

##n=int(input("Ingrese un número: "))
##factorial=1
##for i in range(1,n+1):
##    factorial=factorial*i
##print(factorial)

##n=input("Ingrese un número entero: ")
##digitos=0
##for i in n:
##    digitos=digitos+1
##print(digitos)
    

##i=0
##while i<5:
##    palabra=input("Ingrese una palabra: ")
##    número=int(input("Ingrese un número: "))
##    print(palabra * número)
##    i=i+1

##for i in range(5):
##    palabra=input("Ingrese una palabra: ")
##    número=int(input("Ingrese un número: "))
##    print(palabra*número)

##cadena=input("Ingrese una palabra: ")
##mismaletra=0
##larga=0
##corta=9999
##while cadena!= "FIN":
##    letra=input("Ingrese una letra: ")
##    if cadena[0]==letra:
##        mismaletra=mismaletra+1
##    if larga<len(cadena):
##        larga=len(cadena)
##        largo=cadena
##    if corta>len(cadena):
##        corta=len(cadena)
##        corto=cadena
##    cadena=input("Ingrese una palabra: ")
##print( "La cantidad de palabras que ingresan con la letra ingresada son: ", mismaletra)
##print("La palabra más larga es: ",largo)
##print("La cadena más corta es: ",corto)

##largo=0
##for i in range(5):
##    cadena=input("Ingrese una palabra: ")
##    if largo<len(cadena):
##        largo=len(cadena)
##        larga=cadena
##print("La palabra más larga es : ",larga)
    
##n=float(input("Ingrese un número decimal: "))
##suma=0
##while n!=-1:
##    suma=suma+n
##    n=float(input("Ingrese un número decimal: "))
##print("La suma de sus números es: ",suma)

##for suerte in ("Alesio","Maddi"):
##    print("Mucha suerte mañana",suerte)

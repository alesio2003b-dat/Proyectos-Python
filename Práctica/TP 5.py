##Ejercicio 1
##for i in range(1,20,2):
##    print(i)
##--------------------------------------------------------------------------------
##Ejercicio 2
##i=list(range(1,20,2))
##print(i)
##--------------------------------------------------------------------------------
##Ejercicio 3
##suma=0
##for i in range(10):
##    n=float(input("Ingrese un número: "))
##    suma=suma+n
##print("La suma de sus valores dá como resultado: ",suma)
##----------------------------------------------------------------------------------
##Ejercicio 4
##for i in range(5):
##    n=int(input("Ingrese un número entero: "))
##    if n%2==0:
##        print("El número ",n, "es par")
##    else:
##        print("El número ",n,"es impar")
##-----------------------------------------------------------------------------------
##Ejercicio 5
##for i in range(5):
##    print("El resultado de sumarle 10 a ",i, "es", i+10)
##--------------------------------------------------------------------------------
##Ejercicio 6
##for i in range(100):
##    if i%7==0:
##        print(i)
##-----------------------------------------------------------------------------------
##Ejercicio 7
##n=input("Ingrese una palabra: ")
##vocal=0
##for L in range(len(n)):
##    if n[L]=="a":
##        vocal=vocal+1
##    elif n[L]=="e":
##        vocal=vocal+1
##    elif n[L]=="i":
##        vocal=vocal+1
##    elif n[L]=="o":
##        vocal=vocal+1
##    elif n[L]=="u":
##        vocal=vocal+1
##print(vocal)
##--------------------------------------------------------------------------------
##Ejercicio 8
##for i in range(1,40,2):
##    print(i)
##--------------------------------------------------------------------------------
##Ejercicio 9
##i=list(range(1,40,2))
##print(i)
##--------------------------------------------------------------------------------
##Ejercicio 10
##i=list(range(0,100,7))
##print(i)
##--------------------------------------------------------------------------------
##Ejercicio 11
##for i in range(5):
##    cadena=input("Ingrese una palabra: ")
##    número=int(input("Ingrese un número entero: "))
##    print(cadena*número)
##--------------------------------------------------------------------------------
##Ejercicio 12
##largo=0
##for i in range(5):
##    cadena=input("Ingrese una palabra: ")
##    número=int(input("Ingrese un número entero: "))
##    if largo<len(cadena):
##        largo=len(cadena)
##        larga=cadena
##    print(cadena*número)
##print("La cadena más larga es: ", larga)
##--------------------------------------------------------------------------------
##Ejercicio 13
##n=int(input("Ingrese un número entero: "))
##m=n+1
##print("Los divisores de", n, "son:")
##for i in range(1,m):
##    if n%i==0:
##        print(i)
##--------------------------------------------------------------------------------
##Ejercicio 14
##n=int(input("Ingrese un número entero mayor que 0: "))
##factorial=1
##m=n+1
##for i in range(1,n+1):
##    factorial=factorial*i
##print("El factorial de", n, "es:", factorial)
##////////////////////////////////////////////////////////////////////////////////

numero=int(input("Ingrese un número entero: "))
for i in range(1,numero+1):
    if numero%i==0:
        print(i)

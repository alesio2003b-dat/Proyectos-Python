#Los ejercicios del 1 al 5 los saltee/saltie (como se escriba) pq no eran complicados.
#Ejercicio 6 
#x=int(input("Ingrese un número entero: "))
#divisores= [0]
#for i in range(1,x):
#    if x%i==0:
#        divisores.append(i)

#divisores.remove(0)
#if sum(divisores)>x:
#    print("El número ",x, "es un número abundante, sus divisores son: ",divisores, "y su suma es: ", sum(divisores))
#elif sum(divisores)==x:
#    print("El número ",x, "es un número perfecto, sus divisores son: ",divisores, "y su suma es: ", sum(divisores))
#else:
#    print("El número ",x, "es un número deficiente, sus divisores son: ",divisores, "y su suma es: ", sum(divisores))

########################################

#Ejercicio 7
#Todos los números perfectos entre 2 y 10000
#divisores=[0]
#perfectos=[0]
#for i in range(2,10001):
#    for j in range(1,i):
#        if i%j==0:
#            divisores.append(j)
#    if sum(divisores)==i:
#         perfectos.append(i)
#    divisores= [0]
#perfectos.remove(0)
#rint("La suma de los números perfectos entre 2 y 10000 es: ",sum(perfectos))
#print(perfectos)

####################################################
#Ejercicio 9
#x2 + y2 =n
#n=int(input("Ingrese un número entero: "))
#hola=[0]
#yes=[0]

#for i in range(1,n):
#    for j in range(1,n):
#        if i**2 + j**2==n:
#            hola.append(i)
#            yes.append(j)
#hola.remove(0)
#yes.remove(0)
#c=len(hola)
#print(hola)
#print(yes)

#for e in range(0,c):
#    print("Las posibles combinaciones de x e y son: ", hola[e], "y", yes[e])

#####################
#Ejercicio 11
#Raíz cúbica de un número
x=int(input("Ingrese un número entero: "))
epsilon = 0.01
num_intentos, bajo = 0, 0
alto = max(1, abs(x))
res = (alto + bajo)/2
while abs(res**3 - abs(x)) >= epsilon:
   #print("bajo =", bajo, "alto =", alto, "res =", res)
   num_intentos += 1
   if res**3 < abs(x):
       bajo = res
   else:
       alto = res
   res = (alto + bajo) / 2

if x<0:
   res=-res
# print("numero de intentos =", num_intentos)
# print(res, "está cerca de la raíz cuadrada de", x)

##############################################################################3
#Ejercicio 12
#Polinomio
a=float(input("Ingrese un número 'a' que sea menor a la raíz que busca: " ))
b=float(input("Ingrese un número 'b' que sea mayor a la raíz que busca: " ))
tolerancia=float(input("Tolerecia: "))
contador=0


I = abs(b-a)/2 #la mitad de la diferencia entre a y b 
m = (a+b)/2 #promedio


if -1>0:
    print("El número que busca no se encuntra entre a y b")
    #print('Quiere decir que el número que busca no se encuentra entre a y b ')
else:
    while (I > tolerancia) and (contador < 10000):
        if (a**3-2*a**2-3*a+2)*(m**3-2*m**2-3*m+2)<0:
            b=m
        elif (b**3-2*b**2-3*b+2)*(m**3-2*m**2-3*m+2)<0:
            a=m
        else:
            break
        contador = contador + 1
        I = I/2
        m = a + I

if (contador == 10000):
   print('Se alcanzo el nro maximo de iteraciones')
else:
   print(f'La solucion es: {m}')

print(f"Se requirieron {contador} iteraciones")

print("Corroboración: ",(m**3-2*m**2-3*m+2))

#Ejercicio 13
x=int(input("Ingrese un número entero: "))
cota_inf = 0
while 2**cota_inf < x:
    cota_inf += 1
    bajo = cota_inf - 1
    alto = cota_inf + 1
# Realizar busqueda por biseccion
res = (alto + bajo)/2
while abs(2**res - x) >= epsilon:
    if 2 ** res < x:
        bajo = res
    else:
        alto = res
        res = (alto + bajo)/2
# print(res, "esta cerca de log base 2 de", x)

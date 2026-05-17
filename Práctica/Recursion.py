
# def conv(n):
#     if n==1:
#         r=1
#     else:
#         r=1/n +conv(n-1)
#     return r
# print(conv(3))

###########################
#Problema de conejas:
# def con(n):
#     """ Supone cosas """
#     if n==0:
#         a=1
#     if n==1:
#         a=1
#     # if n==2:
#     #    print(1)
#     if n>1:
#         a= con(n-1)+con(n-2)
#     return a
# # print(con(7))

##########################
# def palindromo(s):
#     if len(s)<=1:
#         return True
#     else: 
#         return s[0]==s[-1] and palindromo(s[1:-1])

# def pasarsololetras(s):
#     """Funcion que pasa a minusculas una palabra y quita todos los espacios , numeros y cosas que no sean letras."""
#     s=s.lower() #Pone en minuscula los caracteres de s
#     letters= ""
#     for i in s:
#         if i.islower(): #Elimina las cosas que no sean caracterés. islower es si algún caracter no es minuscula.
#             letters = letters + i #Concatena las cosas y como letters está en vacío al inicio, no pasa nada.
#     return letters

# def pallindromo(s):
#     print(pasarsololetras(s))
#     return palindromo(pasarsololetras(s))
# print(pallindromo("radar          radar"))

##########################
#Variable global
#poner: global nombrevariable
#hacer cosas variables
# def con(n):
#     global b #Para contar cuantas veces corre la funcion
#     b +=1
#     """ Supone cosas """
#     if n==0:
#         a=1
#     if n==1:
#         a=1
#     #if n==2: #Para contar cuantas veces se llama a con(2). 
#        #print(1) #Imprime un 1 cada vez que pasa
#     if n>1:
#         a= con(n-1)+con(n-2)
#     return a
# def testcon(n):
#     for i in range(n+1):
#         global b
#         b=0
#         print("fib de", i, "=", con(i))
#         print("Cantidad de veces que llamé a con: ", b)
    
# print(testcon(7))

##########################
#Suma de gauss
# def gauss(n):
#     if n==1:
#         r=1
#     else: 
#         r= n + gauss(n-1)
#     return r
# print(gauss(5))

###########################
#Cantidad de digitos
# def digitos(n):
#     if n<10:
#         r=1
#     else:
#         r=1+digitos(int(n/10))
#     return r
# print(digitos(10000))
############################
#Cociente 
# def cociente(a,b):
#     if a>=b:
#         r=cociente(a-b,b)+1
#     else:
#         r=0
#     return r
# print(cociente(178,2))
#############################
#Sumar lista
# def sumarlista(l):
#     if len(l)==0:
#         r=0
#     else:
#         r= l[-1]+sumarlista(l[0:(len(l)-1)])
#     return r
# l=[1,2,3,4,5,6,7,8]
# print(sumarlista(l))
#############################
#Sumar digitos en valor
# def sumardig(n):
#     n=str(n)
#     if len(n)==0:
#         r=0
#     else:
#         r=int(n[-1]) + sumardig(n[0:(len(n)-1)])
#     return r
# print(sumardig(452))
#############################
#Potencia
# def potencia(a,b):
#     if b==0:
#         r=0
#     if b==1:
#         r=a
#     else:
#         r= a*potencia(a,b-1)
#     return r
# print(potencia(2,3))
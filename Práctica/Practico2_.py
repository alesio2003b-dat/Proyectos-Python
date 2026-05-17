# Ejercicio 1
# Desarrolle una función recursiva (sin usar bucles) maxval(L) que reciba una lista L de números 
# y que retorne el máximo valor de la lista (no debe usar la función intrínseca max).
# Por ejemplo, maxval([47, 15, 83, 32, 60, 74, 6, 91, 28, 91, 54]) deberá retornar 91

def maxval(L):
    """La función maxval(L) recibe como argumento una lista L de números y retorna el máximo valor de la lista. Si se ingresa una lista vacía, la función retornará None"""
    if len(L)==0:
        return None
    else:
        L.sort(reverse=True)
    if len(L)==1:
        r=L[0]
    else:
        r=maxval(L[:len(L)-1]) 
    return r

# Ejemplo de uso:
#print(maxval([1,2,3,4,1,402,5,46,3,2,4,-12,401,0,0,-4010,12]))
# import inspect
# print("Uso alguna instrucción prohibida: ")
# print(not any([x in inspect.getsource(maxval) for x in ('while', 'for', 'max')]))
# del inspect

# Ejercicio 2
# En el marco de una implementación de un sistema de gestión escolar, 
# se requiere la creación de una función en Python que permita cargar 
# las notas de los alumnos desde un archivo en formato CSV. La clase Alumno 
# ya está definida con los siguientes atributos y métodos:

class Alumno(object):
    def __init__(self, nombre, apellido):
        """Constructor de la clase. Recibe nombre y apellido."""
        self._nombre = nombre
        self._apellido = apellido
        self._notas = []
        self._promedio = 0
    def __str__(self):
        """Representa el objeto como una cadena de texto."""
        return f'Nombre y apellido: {self._nombre} {self._apellido} | Promedio: {self._promedio}'
    def agregar_notas(self, notas):
        """Recibe una lista de notas, las almacena en _notas y actualiza el promedio."""
        for nota in notas:
            self._notas.append(nota)
        self.actualizar_promedio()
    def actualizar_promedio(self):
        """Actualiza el promedio del alumno."""
        self._promedio = sum(self._notas) / len(self._notas)

# Se solicita implementar la función cargar_alumnos(nombre_archivo) que tome 
# como parámetro el nombre de un archivo CSV y retorne una lista de objetos
# de la clase Alumno. Cada línea del archivo representa un alumno con sus 
# notas, separadas por comas. Por ejemplo:

# Juan,Perez,7,8,9
# Maria,Gomez,6,7,8

# La función deberá leer el archivo, crear objetos de la clase Alumno con los 
# datos proporcionados y retornar una lista con dichos objetos.

def cargar_alumnos(nombre_archivo):
    """Esta función se encarga de leer un archivo donde se encuentran el nombre, apellido y notas de un alumno separados por comas, y devuelve una lista de objetos del tipo Alumno creados con los datos proporcionados"""
    notaas=[]
    objetos=[]

    with open(nombre_archivo,"r") as algo:
        h=0
        for i in algo:
            a=i.strip().split(",")
            b=Alumno(a[0],a[1])
            for i in a[2:]:
                notaas.append(float(i))    
            b.agregar_notas(notaas)
            objetos.append(b)
            notaas=[]
    return objetos
#Preguntas si agrego las notas o no.
# Ejemplo de uso:
# alumnos = cargar_alumnos('archivo_notas.csv')
# for alumno in alumnos:
#     print(type(alumno),alumno)

# # Ejercicio 3
# # El coloreo  de un grafo es asignar un "color" a cada nodo de modo que nodos 
# # conectados no tienen el mismo "color". Por ejemplo, un grafo con las aristas
# # A->B
# # B->C
# # C->A
# # cuyos nodos A, B y C tienen el color verde, azul y rojo 
# # respectivamente, el grafo tienen un coloreo válido,
# # mientras que si los nodos A, B y C tienen el color verde, azul y verde
# # respectivamente, el grafo no tiene un coloreo válido (ya que los nodos A y C 
# # tienen el mismo color y están conectados por la arista C->A).
# # Las clases Nodo, Arista y GrafoDirigido a usar ya se encuentran definidas a continuación:

class Nodo(object):
    def __init__(self, nombre, color=''):
        """Supone que el nombre y color es una cadena"""
        self._nombre = nombre
        self._color = color # atributo nuevo

    def obtener_nombre(self):
        return self._nombre
    
    def obtener_color(self): # función nueva
        return self._color
    
    def __str__(self):
        return self._nombre

class Arista(object):
    def __init__(self, origen, destino):
        """Supone que origen y destino son nodos"""
        self._origen = origen
        self._destino = destino

    def obtener_origen(self):
        return self._origen
    
    def obtener_destino(self):
        return self._destino
    
    def __str__(self):
        return self._origen.obtener_nombre() + '->' + self._destino.obtener_nombre()
    
    def __eq__(self, otro):
        return self._origen == otro._origen and self._destino == otro._destino 

class GrafoDirigido(object):
    # nodos es una lista de los nodos en el grafo
    # aristas es un diccionario que asigna a cada nodo una lista de sus hijos
    def __init__(self):
        self._nodos = []
        self._aristas = {}
    
    def agregar_nodo(self, nodo):
        if nodo in self._nodos:
            raise ValueError('Nodo duplicado')
        else:
            self._nodos.append(nodo)
            self._aristas[nodo] = []
    
    def agregar_arista(self, arista):
        origen = arista.obtener_origen()
        destino = arista.obtener_destino()
        if not (origen in self._nodos and destino in self._nodos):
            raise ValueError('Nodo no está en el grafo')
        self._aristas[origen].append(destino)
           
    def __str__(self):
        resultado = ''
        for origen in self._nodos:
            for destino in self._aristas[origen]:
                resultado = (resultado + origen.obtener_nombre() + '->'
                            + destino.obtener_nombre() + '\n')
        return resultado[:-1]  # omitir el salto de línea final

    def tiene_coloreo(self):
        colores=[]
        for i in self._nodos:
            for j in self._aristas[i]:
                colores.append(j.obtener_color())
            if i.obtener_color() in colores:
                return False
            colores=[]
        return True
        
# se agregó un nuevo atributo ._color a la clase Nodo de modo que además del 
# nombre, los objetos de clase Nodo tengan un color.
# se solicita modificar el método tiene_coloreo de la clase NodoDirigido de modo que
# devuelva True si el grafo tiene un coloreo válido (es decir, que nodos conectados tienen distinto color)
# y devuelva False en caso contrario (es decir, al menos un par de nodos conectados tienen el mismo color).

# Ejemplo de uso
# nA, nB, nC = Nodo('A', 'azul'), Nodo('B', 'amarillo'), Nodo('C', 'rojo') # nodos
# a1, a2, a3 = Arista(nA, nB), Arista(nB, nC), Arista(nC, nA) # aristas

# g1 = GrafoDirigido() # creo grafo
# for n in (nA, nB, nC):
#     g1.agregar_nodo(n) # agrego nodos
# for a in (a1, a2, a3):
#     g1.agregar_arista(a) # agrego aristas
# print(g1.tiene_coloreo()) # probar cambiando los colores de los nodos

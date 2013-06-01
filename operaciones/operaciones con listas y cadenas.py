Listas

Python utiliza varios tipos de datos compuestos, que se utilizan para agrupar otros valores. El m�s vers�til es la lista, que se puede escribir como una lista de valores (elementos) separada por comas entre corchetes. Los elementos de una lista no tienen que ser todos del mismo tipo.

>>> a = ['fiambre', 'huevos', 100, 1234]
>>> a
['fiambre', 'huevos', 100, 1234]

Como los �ndices de las cadenas, los �ndices de una lista empiezan en cero. Las listas tambi�n se pueden cortar, concatenar, etc.:

A diferencia de las cadenas, que son inmutables, es posible cambiar los elementos de una lista:

>>> a
['fiambre', 'huevos', 100, 1234]
>>> a[2] = a[2] + 23
>>> a
['fiambre', 'huevos', 123, 1234]

 Se puede asignar a un corte, lo que puede hasta cambiar el tama�o de la lista:

>>> # Reemplazar elementos:
... a[0:2] = [1, 12]
>>> a
[1, 12, 123, 1234]
>>> # Quitar elementos:
... a[0:2] = []
>>> a
[123, 1234]
>>> # Insertar cosas:
... a[1:1] = ['puaj', 'xyzzy']
>>> a
[123, 'puaj', 'xyzzy', 1234]
>>> a[:0] = a     # Insertarse (una copia) al principio de ella misma
>>> a
[123, 'puaj', 'xyzzy', 1234, 123, 'puaj', 'xyzzy', 1234]

 Es posible anidar listas (crear listas que contienen otras listas), por ejemplo:

>>> q = [2, 3]
>>> p = [1, q, 4]
>>> len(p)
3
>>> p[1]
[2, 3]
>>> p[1][0]
2
>>> p[1].append('xtra')    
>>> p
[1, [2, 3, 'xtra'], 4]
>>> q
[2, 3, 'xtra']


M�s sobre las listas

El tipo de datos ``lista'' tiene algunos m�todos m�s. �stos son todos los m�todos de los objetos lista:

append(x)
    A�ade un elemento al final de una lista; es equivalente a a[len(a):] = [x]. 

extend(L)
    Extiende la lista concaten�ndole todos los elementos de la lista indicada; es equivalente a a[len(a):] = L. 

insert(i, x)
    Inserta un elemento en un posici�n dada. El primer argumento es el �ndice del elemento antes del que se inserta, por lo que a.insert(0, x) inserta al principio de la lista y a.insert(len(a), x) equivale a a.append(x). 

remove(x)
    Elimina el primer elemento de la lista cuyo valor es x. Provoca un error si no existe tal elemento. 

pop([i])
    Elimina el elemento de la posici�n dada de la lista y lo devuelve. Si no se especifica un �ndice, a.pop() devuelve el �ltimo elemento de la lista y tambi�n lo elimina. Los corchetes que rodean la i en la signatura del m�todo indican que el par�metro es opcional, no que haya que teclear los corchetes en dicha posici�n. Esta notaci�n es frecuente en la Referencia de las bibliotecas de Python. 

index(x)
    Devuelve el �ndice de el primer elemento de la lista cuyo valor sea x. Provoca un error si no existe tal elemento. 

count(x)
    Devuelve el n�mero de veces que aparece x en la lista. 

sort()
    Ordena ascendentemente los elementos de la propia lista (la lista queda cambiada). 

reverse()
    Invierte la propia lista (la lista queda cambiada). 

Un ejemplo que utiliza varios m�todos de la lista:

>>> a = [66.25, 333, 333, 1, 1234.5]
>>> print a.count(333), a.count(66.25), a.count('x')
2 1 0
>>> a.insert(2, -1)
>>> a.append(333)
>>> a
[66.25, 333, -1, 333, 1, 1234.5, 333]
>>> a.index(333)
1
>>> a.remove(333)
>>> a
[66.25, -1, 333, 1, 1234.5, 333]
>>> a.reverse()
>>> a
[333, 1234.5, 1, 333, -1, 66.25]
>>> a.sort()
>>> a
[-1, 1, 66.6, 333, 333, 1234.5]


C�mo usar las listas como pilas

Los m�todos de las listas facilitan mucho usar una lista como una pila, donde el �ltimo elemento a�adido es el primer elemento recuperado. (``last-in, first-out'', ``�ltimo en llegar, primero en salir''). Para apilar un elemento, usa append(). Para recuperar el elemento superior de la pila, usa pop() sin un �ndice expl�cito. Por ejemplo:

>>> pila = [3, 4, 5]
>>> pila.append(6)
>>> pila.append(7)
>>> pila
[3, 4, 5, 6, 7]
>>> pila.pop()
7
>>> pila
[3, 4, 5, 6]
>>> pila.pop()
6
>>> pila.pop()
5
>>> pila
[3, 4]


C�mo usar las listas como colas

Tambi�n es muy pr�ctico usar una lista como cola, donde el primer elemento que se a�ade a la cola es el primero en salir (``first-in, first-out'', ``primero en llegar, �ltimo en salir''). Para a�adir un elemento al final de una cola, usa append(). Para recuperar el primer elemento de la cola, usa pop() con 0 de �ndice. Por ejemplo:

>>> cola = ["Eric", "John", "Michael"] 
>>> cola.append("Terry")           # llega Terry
>>> cola.append("Graham")          # llega Graham
>>> cola.pop(0)
'Eric'
>>> cola.pop(0)
'John'
>>> cola
['Michael', 'Terry', 'Graham']


Herramientas de programaci�n funcional

Hay tres funciones internas que son muy �tiles al tratar con listas: filter(), map() y reduce().

"filter(funci�n, secuencia)", filtrar, devuelve una secuencia (del mismo tipo, si es posible) que contiene aquellos elementos de la secuencia de entrada para los que funci�n(elemento) resulta verdadero. Por ejemplo, para calcular algunos primos:

>>> def f(x): return x % 2 != 0 and x % 3 != 0
...
>>> filter(f, range(2, 25))
[5, 7, 11, 13, 17, 19, 23]

"map(funci�n, secuencia)", transformar, llama a funci�n(elemento) para cada uno de los elementos de la secuencia y devuelve una lista compuesta por los valores resultantes. Por ejemplo, para calcular algunos cubos:

>>> def cubo(x): return x*x*x
...
>>> map(cubo, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

Se puede pasar m�s de una secuencia como par�metro. La funci�n debe tener tantos argumentos como secuencias se le pasan y se llama a la funci�n con el valor correspondiente de cada secuencia de entrada (o None si una secuencia es m�s corta que otra). Por ejemplo:

>>> secuencia = range(8)
>>> def suma(x,y): return x+y
...
>>> map(suma, secuencia, secuencia)
[0, 2, 4, 6, 8, 10, 12, 14]

"reduce(func, secuencia)",reducir, devuelve un valor simple que se construye llamando a la funci�n binaria func con los dos primeros elementos de la secuencia, luego con el resultado y el siguiente elemento y as� sucesivamente. Por ejemplo, para calcular la suma de los n�meros de 1 a 10:

>>> def suma(x,y): return x+y
...
>>> reduce(suma, range(1, 11))
55

Si s�lo hay un elemento en la secuencia, se devuelve su valor; si la secuencia est� vac�a, se lanza una excepci�n.

Se puede pasar un tercer argumento para indicar el valor inicial. En este caso, se devuelve este valor inicial para la secuencia vac�a y la funci�n se aplica al primer elemento, luego al segundo y as� sucesivamente. Por ejemplo,

>>> def sum(secuencia):
...     def suma(x,y): return x+y
...     return reduce(suma, secuencia, 0)
... 
>>> sum(range(1, 11))
55
>>> sum([])
0


La sentencia del

Hay un modo de eliminar un elemento de una lista dado su �ndice en lugar de su valor: la sentencia del. Tambi�n se puede utilizar para eliminar cortes de una lista (lo que hac�amos antes asignando una lista vac�a al corte). Por ejemplo:

>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]

del se puede utilizar para eliminar variable completas:

>>> del a

Hacer referencia al nombre a a partir de aqu� provoca un error (al menos hasta que se asigne otro valor al nombre).



Mas sobre las listas.


En Python todo es un objetos, por lo que cuando definimos una cadena estamos definiendo un objeto.
Como hemos visto toda clase tiene una serie de m�todos, veremos los m�todos principales que tiene la clase que en Python administra una cadena.

Los m�todos:
    
capitalize()
Retorna otra cadena con el primer caracter en may�sculas.

cadena='ana'
print cadena.capitalize() #Ana
print cadena  #ana

Es importante notar que no se modifica el contenido de la variable 'cadena'. El m�todo capitalize() retorna otra cadena con el primero en may�sculas.

upper()
Retorna otra cadena con todos los caracteres convertidos a may�scula.
	cadena1='ana'
cadena2=cadena1.upper()
print cadena2               #ANA

lower()
Retorna otra cadena con todos los caracteres convertidos a min�sculas.

cadena1='Ana'
cadena2=cadena1.lower()
print cadena2               #ana

isupper()
Retorna True si todos los caracteres de la cadena est�n en may�sculas.

cadena='ANA'
if cadena.isupper():
    print 'La cadena '+cadena+' esta toda en mayusculas'

islower()
Retorna True si todos los caracteres de la cadena est�n en min�sculas.

cadena1='ana'
if cadena.islower():
    print 'La cadena '+cadena+' esta toda en minusculas'

isdigit()
Retorna verdadero si todos los caracteres de la cadena son d�gitos.

cadena='120'
if cadena.isdigit():
    print 'Todos los caracteres de la cadena son numeros'

Si al menos uno de los caracteres es distinto a un d�gito retorna False. Inclusive si tiene el caracter punto.

isalpha()
Retorna True si todos los caracteres son alfab�ticos.

cadena='Hola Mundo'
if cadena.isalpha():
    print 'Todos los caracteres de la cadena son del alfabeticos'
else:
    print 'No todos los caracteres de la cadena son del alfabeticos'

En el ejemplo superior ejecuta el bloque del else ya que la cadena contiene un caracter de espacio.


isspace()
Retorna verdadero si todos los caracteres de la cadena son espacios en blanco

cadena='   '
if cadena.isspace():
    print 'Todos los caracteres de la cadena son espacios en blanco'


isalnum()
Retorna True si todos los caracteres de la cadena son n�meros o caracteres alfab�ticos.

cadena='cordoba2008'
if cadena.isalnum():
    print 'Todos los caracteres son numeros o alfabeticos'

find('cadena',[inicio],[fin])
Retorna la posici�n donde se encuentra el valor del primer par�metro en el string. Si no se encuentra retorna -1. Podemos indicar como segundo y tercer par�metro a partir de que posici�n y hasta que posici�n de la cadena hacer la b�squeda.

cadena='esto es una prueba y es solo eso'
pos=cadena.find('es')
print pos   #0

Retorna 0 ya que los dos primeros caracteres son la cadena 'es', es decir retorna la primera aparici�n del string.

cadena='esto es una prueba y es solo eso'
pos=cadena.find('es',5)
print pos   #5

En este otro ejemplo comenzamos la b�squeda a partir de la posici�n 5. Si no indicamos el tercer par�metro la b�squeda la hace hasta el final de la cadena

rfind('cadena',[inicio],[fin])

Igual al m�todo find con la diferencia que la b�squeda comienza desde el final.

cadena='esto es una prueba y es solo eso'
pos=cadena.rfind('es')
print pos  #29
count('cadena',[inicio],[fin])
Retorna la cantidad de veces que la cadena se repite en el string.

cadena='esto es una prueba y es solo eso'
cant=cadena.count('es')
print cant   #4

replace('cadena1','cadena2',[maximo])
Retorna un string remplazando todas las ocurrencias de cadena1 por cadena2. Podemos eventuamente indicar la cantidad m�xima de remplazos.

cadena1='esto es una prueba y es solo eso'
cadena2=cadena1.replace('es','ES')
print cadena2  #ESto ES una prueba y ES solo ESo 

split('caracter separador',[maximo])
El m�todo split retorna una lista dividiendo el string por el caracter indicado en el primer par�metro. Podemos pasar un segundo par�metro indicando la cantidad de trozos a general, el �ltimo elemento de la lista almacena el resto del string.

cadena='esto es una prueba y es solo eso'
lista=cadena.split(' ')
print lista               #['esto', 'es', 'una', 'prueba', 'y', 'es', 'solo', 'eso']
print len(lista)          #8
lista=cadena.split(' ',2) 
print lista               #['esto', 'es', 'una prueba y es solo eso'] 
print len(lista)          #3

rsplit('caracter separador',[maximo])
Semejante a split pero procesando desde el final del string. En caso de indicar maximo el primer elemento de la lista almacena el trozo restante.

cadena='esto es una prueba y es solo eso'
lista=cadena.rsplit(' ')
print lista               #['esto', 'es', 'una', 'prueba', 'y', 'es', 'solo', 'eso']
print len(lista)          #8
lista=cadena.rsplit(' ',2) 
print lista               #['esto es una prueba y es', 'solo', 'eso'] 
print len(lista)          #3


splitlines()
Retorna una lista dividiendo el string con los retornos de carro contenidos en el mismo.

mensaje="""Primer linea
           Segunda linea
           Tercer linea
           Cuarta linea"""

lista=mensaje.splitlines()
print lista #['Primer linea', ' Segunda linea', ' Tercer linea', ' Cuarta linea'] 


swapcase()
Retorna un string transformando los caracteres min�sculas a may�sculas y los may�sculas a min�sculas.

cadena1='Sistema de Facturacion'
cadena2=cadena1.swapcase()
print cadena2        #sISTEMA DE fACTURACION 


rjust(ancho,caracter de relleno)
Retorna un string justificado a derecha y rellenando el lado izquierdo con caracteres seg�n el segundo par�metro. La nueva cadena toma un largo indicado seg�n el valor del primer par�metro.

cadena='200'
cadena2=cadena.rjust(5,'$')
print cadena2   #$$200


ljust(ancho,caracter de relleno)
Similar a rjust con la salvedad que se justifica a derecha el string.

cadena='200'
cadena2=cadena.ljust(5,'$')
print cadena2   #200$$


center(ancho,caracter de relleno)
El string original se centra.
cadena='200'
cadena2=cadena.center(5,'$')
print cadena2   #$200$

 eso es todo lo que pude averiguar sobre las listas metodos y formas de combinarlas para hacer un mejor uso con ellas no ice copy paste ok o bien jajaja pero lo lei...

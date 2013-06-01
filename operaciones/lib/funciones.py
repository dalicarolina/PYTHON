from lib.operaciones import *
from lib.operaciones import HttpRequestResponseRedirect as RE

valor =int(raw_input('ingrese un valor'))
valor2 =int(raw_input('ingrese otro valor'))
operacion=raw_input('que operacion desea realizar: {s - r- m - d}')

if operacion.lower()=='s':
    print suma(valor,valor2)

elif operacion.lower()=='r':
    print resta(valor,valor2)

elif operacion.lower()=='m':
    print multiplicacion(valor,valor2)

elif operacion.lower()=='d':
    print division(valor,valor2)

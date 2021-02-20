import re

_array = []
texto = "**Node.js** es un **entorno** **en** tiempo de ejecución **en** multiplataforma, **de** código abierto, para la capa del servidor basado en el lenguaje de programación **JavaScript** asíncrono, con E/S **de** datos en una arquitectura orientada a eventos y basado en el motor V8."

expresion = (re.split(r'\s', texto))

for letra in expresion:
    if letra[0] == '*':
        _array.append(letra[2:-2])
        _array = list(set(_array))
print(_array)


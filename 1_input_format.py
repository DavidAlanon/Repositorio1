"""
Ejemplo para pedir input de usuario y formatear la respuesta
"""

PREGUNTA = '¿Cómo te llamas? '
RESPUESTA = input(PREGUNTA)

SALUDO = 'Bienvenido al curso de Python'
print('Hola', RESPUESTA, '¿cómo estás?')

RESPUESTA_FORMATEADA = 'Hola {}, {}'.format(RESPUESTA, SALUDO)

print(RESPUESTA_FORMATEADA)

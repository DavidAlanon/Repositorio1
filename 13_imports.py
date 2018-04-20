"""
Ejemplos de cómo importar módulos y funciones en python
"""

import utils # Nos permite importar todas las funciones

utils.sumar(6, 8)
utils.restar(10, 4)

from utils import sumar # Esto es para importar únicamente la función que queramos

sumar (2, 2)

from libs import bombing
bombing.where_are_the_bombs()
bombing.explosion

from libs.bombing import * # El asterisco permite importar todo lo que esté en el archivo, en este caso "bombing"
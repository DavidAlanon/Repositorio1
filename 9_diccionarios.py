"""
Ejemplos para trabajar con diccionarios
"""

ALUMNO = {
    'nombre': 'David',
    'edad': 27,
    'clase': 'python'
}

print(ALUMNO)
print(ALUMNO['nombre'])
print(ALUMNO['edad'])
ALUMNO['edad'] = 25
print(ALUMNO)
ALUMNO['sexo'] = 'masculino'
print(ALUMNO)
del ALUMNO['sexo']
print(ALUMNO)

ALUMNO.clear()
print(ALUMNO)


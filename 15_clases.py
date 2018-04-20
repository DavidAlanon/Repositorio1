"""
Trabajando con clases y POO (Programación Orientada a Objetos)
"""

class Thing: 
    pass

cosa = Thing()

class Fruit: 
    def __init__(self):
        print('objeto fruta iniciado') 

fruit = Fruit()

# Argumentos del constructor

class Person: 
    """ Esta es la documentación de la clase Person """
    COUNTER= 0

    def __init__(self, name):
        self.name = name
        self.knowledge = []
        Person.COUNTER += 1


    def __str__(self):
        return 'Me llamo {} y se: {}'.format(self.name, self.knowledge)

    def learn(self,what):
        self.knowledge.append(what)






p1 = Person('David')
p2 = Person ('Mary')
p3 = Person ('Diego')

p1.learn('python')
p2.learn('javascript')
p3.learn('C#')

print(p1)
print(p2)
print(p3)
print(Person.COUNTER)


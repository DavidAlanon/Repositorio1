from django.db import models

class Player(models.Model):
    name = models.CharField('Nombre',max_length=40)
    gender = models.BooleanField('Sexo')
    power = models.IntegerField('Poder')
    lives = models.IntegerField('Vidas')
    gems = models.IntegerField('Gemas')

    def __str__(self):
        return self.name 

        verbose_name = 'Jugadores'
        verbose_name_plural = 'Jugadores'
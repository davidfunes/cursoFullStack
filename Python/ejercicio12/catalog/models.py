from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=24)
    family_name = models.CharField(max_length=64)
    born = models.DateField(null=True)
    died = models.DateField(null=True, blank=True)


    def __str__(self):
        return f'{self.name} {self.family_name}\n'


class Film(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    sinopsis = models.TextField(max_length=1000)


    def __str__(self):
        return f'{self.title} ({self.year})\n'

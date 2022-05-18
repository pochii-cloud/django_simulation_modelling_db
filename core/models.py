from django.db import models

# Create your models here.

Gender_Choices = [
    ('Male', 'M'),
    ('Female', 'F'),
]

Genetic_Variations = [
    ('Mutations', 'M'),
    ('Recombinations', 'R'),
    ('Immigrations', 'I'),
]

Spread_Type = (
    ('Airbone', 'A'),
    ('Waterbone', 'W'),
    ('Communicable', 'C'),

)


class Location(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    population = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(choices=Gender_Choices, max_length=50, default=1)
    Genetic_Variation = models.CharField(choices=Genetic_Variations, max_length=100, default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Epidemic(models.Model):
    name = models.CharField(max_length=150)
    spread_type = models.CharField(max_length=200, choices=Spread_Type, default=1)

    def __str__(self):
        return self.name

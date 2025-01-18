from django.db import models

# Create your models here.

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    picture = models.ImageField(upload_to="pokemon_images", null=True)
    
    def __str__(self)-> str:
        return f'{self.first_name} {self.last_name}'

class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPE = {
        ('A', 'AGUA'),
        ('F', 'FUEGO'),
        ('T','TIERRA'),
        ('P', 'PLANTA'),
        ('E', 'ELECTRICO'),
        ('L', 'LAGARTIJA')
    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPE, null= False)
    weight = models.DecimalField(max_digits=7, decimal_places=4)
    height = models.DecimalField(max_digits=7, decimal_places=4)
    trainer = models.ForeignKey(Trainer, on_delete=models.RESTRICT, null=True)
    picture = models.ImageField(upload_to="pokemon_images")
    
    def __str__(self):
        return self.name    
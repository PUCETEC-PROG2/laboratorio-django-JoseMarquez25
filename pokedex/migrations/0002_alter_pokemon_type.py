# Generated by Django 5.1.4 on 2025-01-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'PLANTA'), ('L', 'LAGARTIJA'), ('F', 'FUEGO'), ('A', 'AGUA'), ('E', 'ELECTRICO'), ('T', 'TIERRA')], max_length=30),
        ),
    ]

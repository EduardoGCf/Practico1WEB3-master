# Generated by Django 5.1.7 on 2025-03-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0004_materia_docente'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='materias_inscritas',
            field=models.ManyToManyField(related_name='alumnos', to='Restaurante.materia'),
        ),
    ]

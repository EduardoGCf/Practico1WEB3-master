# Generated by Django 5.1.7 on 2025-03-25 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0003_docente'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='docente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='Restaurante.docente'),
        ),
    ]

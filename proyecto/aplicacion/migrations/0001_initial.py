# Generated by Django 5.0.3 on 2024-03-24 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=50)),
                ('año_fabricacion', models.IntegerField()),
                ('cilindrada', models.CharField(max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kilometros', models.IntegerField()),
                ('moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.moto')),
            ],
        ),
    ]

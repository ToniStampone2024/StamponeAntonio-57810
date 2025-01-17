# Generated by Django 4.2.13 on 2024-07-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlquilerAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('origen', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('fecha_compra', models.DateField()),
            ],
            options={
                'verbose_name': 'AlquilerAuto',
                'verbose_name_plural': 'AlquilerAutos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('fecha_compra', models.DateField()),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hoteles',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Traslado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('origen', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=4)),
                ('fecha_compra', models.DateField()),
            ],
            options={
                'verbose_name': 'Traslado',
                'verbose_name_plural': 'Traslados',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('origen', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=4)),
                ('fecha_compra', models.DateField()),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]

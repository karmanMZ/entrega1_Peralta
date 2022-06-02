# Generated by Django 4.0.4 on 2022-06-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estilos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('ibu', models.IntegerField()),
                ('alcohol', models.IntegerField()),
                ('cuerpo', models.CharField(max_length=20)),
                ('amargor', models.CharField(max_length=20)),
                ('aroma', models.CharField(max_length=20)),
                ('temp_cons', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('tipo_producto', models.CharField(max_length=40)),
                ('fecha_registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('cargo', models.CharField(max_length=40)),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
    ]
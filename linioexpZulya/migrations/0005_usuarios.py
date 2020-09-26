# Generated by Django 3.1 on 2020-09-23 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200922_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('password', models.CharField(max_length=8)),
                ('dni', models.FloatField(max_length=8)),
                ('nombre', models.TextField()),
                ('apellidoPaterno', models.TextField()),
                ('apellidoMaterno', models.TextField()),
                ('genero', models.CharField(max_length=1)),
                ('fechaNacimiento', models.DateField()),
                ('fechaCreacion', models.DateField()),
            ],
        ),
    ]

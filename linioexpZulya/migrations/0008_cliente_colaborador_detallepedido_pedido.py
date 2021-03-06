# Generated by Django 3.1 on 2020-09-26 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200923_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateField()),
                ('estado', models.TextField()),
                ('fechaEntrega', models.DateField()),
                ('direccionEntrega', models.TextField()),
                ('tarifa', models.FloatField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.cliente')),
                ('colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.colaborador')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pedido')),
            ],
        ),
    ]

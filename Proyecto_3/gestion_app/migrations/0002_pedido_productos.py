# Generated by Django 4.2.1 on 2023-10-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]

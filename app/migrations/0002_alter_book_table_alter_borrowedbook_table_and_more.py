# Generated by Django 5.1.6 on 2025-02-24 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='books',
        ),
        migrations.AlterModelTable(
            name='borrowedbook',
            table='borrowed_books',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-18 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_film_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='died',
            field=models.DateField(blank=True, null=True),
        ),
    ]

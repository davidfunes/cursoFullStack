# Generated by Django 4.1.2 on 2022-10-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_film_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_todolist_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='average',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_todolist_slno'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='average',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todolist',
            name='num1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='num2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='num3',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 2.2 on 2019-07-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Unidade_Central', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiacomponentes',
            name='quantidade_componentes',
        ),
        migrations.AddField(
            model_name='fita',
            name='quantidade_componentes',
            field=models.IntegerField(default=0),
        ),
    ]

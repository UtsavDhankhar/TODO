# Generated by Django 4.0.4 on 2022-05-03 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

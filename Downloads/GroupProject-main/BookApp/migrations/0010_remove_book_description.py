# Generated by Django 2.2 on 2021-05-03 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0009_auto_20210503_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
    ]

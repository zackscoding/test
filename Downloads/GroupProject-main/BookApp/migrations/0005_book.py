# Generated by Django 2.2 on 2021-04-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0004_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=45)),
                ('author', models.CharField(default='', max_length=45)),
                ('yearPublished', models.CharField(default='', max_length=45)),
                ('genre', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('comentario', models.CharField(max_length=1200, verbose_name='Comentário')),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-11-07 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=models.TextField(),
        ),
    ]

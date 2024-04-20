# Generated by Django 4.2.11 on 2024-04-19 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(default='avatares/default.png', upload_to='avatares'),
        ),
        migrations.AlterField(
            model_name='entregable',
            name='entregado',
            field=models.BooleanField(null=True),
        ),
    ]

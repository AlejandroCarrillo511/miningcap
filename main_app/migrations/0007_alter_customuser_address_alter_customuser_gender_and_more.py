# Generated by Django 4.2.7 on 2023-11-21 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_notificationstaff_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.TextField(verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(upload_to='', verbose_name='Imagen de perfil'),
        ),
    ]

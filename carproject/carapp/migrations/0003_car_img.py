# Generated by Django 4.2 on 2023-04-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_rename_cars_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img',
            field=models.ImageField(default='default', upload_to='gallery'),
            preserve_default=False,
        ),
    ]

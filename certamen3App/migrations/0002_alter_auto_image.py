# Generated by Django 4.2.5 on 2023-11-24 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certamen3App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]

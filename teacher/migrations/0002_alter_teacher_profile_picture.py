# Generated by Django 3.2.9 on 2021-11-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='Profile Picture'),
        ),
    ]

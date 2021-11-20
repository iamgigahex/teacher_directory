# Generated by Django 3.2.9 on 2021-11-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=60, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=60, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('profile_picture', models.ImageField(upload_to='profile_images/', verbose_name='Profile Picture')),
                ('room_no', models.CharField(max_length=40, verbose_name='Room Number')),
                ('subjects', models.ManyToManyField(to='teacher.Subject')),
            ],
        ),
    ]

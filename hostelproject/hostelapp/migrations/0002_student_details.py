# Generated by Django 4.1.2 on 2022-11-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]

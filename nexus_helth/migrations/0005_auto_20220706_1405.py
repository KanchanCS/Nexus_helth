# Generated by Django 3.2.6 on 2022-07-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_helth', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]

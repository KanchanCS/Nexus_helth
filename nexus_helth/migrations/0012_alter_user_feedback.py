# Generated by Django 3.2.6 on 2022-07-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_helth', '0011_auto_20220707_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='feedback',
            field=models.TextField(max_length=100),
        ),
    ]

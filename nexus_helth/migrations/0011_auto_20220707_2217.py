# Generated by Django 3.2.6 on 2022-07-07 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_helth', '0010_auto_20220707_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='feedback',
        ),
    ]

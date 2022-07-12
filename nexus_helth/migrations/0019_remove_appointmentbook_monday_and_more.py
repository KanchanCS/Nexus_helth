# Generated by Django 4.0.6 on 2022-07-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_helth', '0018_appointmentbook_monday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentbook',
            name='monday',
        ),
        migrations.AddField(
            model_name='appointmentbook',
            name='week_days',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
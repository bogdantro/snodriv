# Generated by Django 3.1.5 on 2022-02-27 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20210904_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='place',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='zipcode',
        ),
    ]

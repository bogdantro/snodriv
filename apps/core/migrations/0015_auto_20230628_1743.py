# Generated by Django 3.1.5 on 2023-06-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_profile_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=0, max_length=300),
        ),
    ]

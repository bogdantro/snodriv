# Generated by Django 4.1.5 on 2023-07-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default.png', null=True, upload_to='static/images/other/user_images/'),
        ),
    ]

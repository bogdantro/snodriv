# Generated by Django 4.1.5 on 2023-06-27 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default.png', upload_to='other/user_images/'),
        ),
    ]
# Generated by Django 3.1.5 on 2023-07-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20230701_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Densification_alltime_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Densification_day_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Densification_month_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Densification_previous_day_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Densification_week_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Densification_year_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Fiber_alltime_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Fiber_day_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Fiber_month_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Fiber_previous_day_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Fiber_week_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Fiber_year_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='TBB_alltime_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='TBB_day_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='TBB_month_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='TBB_previous_day_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='TBB_week_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='TBB_year_points',
            field=models.IntegerField(default=0),
        ),
    ]
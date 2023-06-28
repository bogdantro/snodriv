from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import tree
from django.utils import timezone

class Result(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    user_image = models.ImageField(blank=True, default='', upload_to='other/user_images/')
    place = models.CharField(max_length=300, blank=True, null=True)
    points = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default='static/images/default.png', upload_to='other/user_images/')
    day_points = models.IntegerField(default=0)
    previous_day_points = models.IntegerField(default=0)
    week_points = models.IntegerField(default=0)
    month_points = models.IntegerField(default=0)
    year_points = models.IntegerField(default=0)
    alltime_points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} sin profil'
    
    def save(self, *args, **kwargs):
        if self.pk:
            # Get the existing week_points if the instance is already saved
            existing_week_points = Profile.objects.get(pk=self.pk).week_points
        else:
            existing_week_points = 0

        # Calculate the increment of day_points
        day_points_increment = self.day_points - self.previous_day_points

        # Update week_points by adding the increment of day_points to existing_week_points
        self.week_points = existing_week_points + day_points_increment

        super(Profile, self).save(*args, **kwargs)
        
        # Update previous_day_points with the current day_points
        self.previous_day_points = self.day_points
        super(Profile, self).save(update_fields=['previous_day_points'])
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import tree
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default='static/images/default.png', upload_to='other/user_images/')
    day_points = models.IntegerField(default=0)
    previous_day_points = models.IntegerField(default=0)
    week_points = models.IntegerField(default=0)
    month_points = models.IntegerField(default=0)
    year_points = models.IntegerField(default=0)
    alltime_points = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} sin profil'

    def save(self, *args, **kwargs):
        day_difference = self.day_points - self.previous_day_points
        month_difference = self.day_points - self.previous_day_points
        year_difference = self.day_points - self.previous_day_points
        alltime_difference = self.day_points - self.previous_day_points
        
        if day_difference > 0:
            self.week_points += day_difference
            self.month_points += month_difference
            self.year_points += year_difference
            self.alltime_points += alltime_difference
        
        self.previous_day_points = self.day_points
        super(Profile, self).save(*args, **kwargs)
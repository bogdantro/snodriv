from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import tree
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TBB = models.BooleanField(default=False)
    # Days
    TBB_day_points = models.IntegerField(default=0)
    TBB_previous_day_points = models.IntegerField(default=0)
    TBB_week_points = models.IntegerField(default=0)
    TBB_month_points = models.IntegerField(default=0)
    TBB_year_points = models.IntegerField(default=0)
    TBB_alltime_points = models.IntegerField(default=0)

    Fiber = models.BooleanField(default=False)
    # Days
    Fiber_day_points = models.IntegerField(default=0)
    Fiber_previous_day_points = models.IntegerField(default=0)
    Fiber_week_points = models.IntegerField(default=0)
    Fiber_month_points = models.IntegerField(default=0)
    Fiber_year_points = models.IntegerField(default=0)
    Fiber_alltime_points = models.IntegerField(default=0)

    Densification = models.BooleanField(default=False)
    # Days
    Densification_day_points = models.IntegerField(default=0)
    Densification_previous_day_points = models.IntegerField(default=0)
    Densification_week_points = models.IntegerField(default=0)
    Densification_month_points = models.IntegerField(default=0)
    Densification_year_points = models.IntegerField(default=0)
    Densification_alltime_points = models.IntegerField(default=0)

    image = models.ImageField(blank=True, default='static/images/default.png', upload_to='other/user_images/')
    day_points = models.IntegerField(default=0)
    previous_day_points = models.IntegerField(default=0)
    week_points = models.IntegerField(default=0)
    month_points = models.IntegerField(default=0)
    year_points = models.IntegerField(default=0)
    alltime_points = models.IntegerField(default=0)
    comp_points = models.IntegerField(default=0)
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
        
         # Calculate TBB_day_points
        tbb_day_difference = self.TBB_day_points - self.TBB_previous_day_points
        if tbb_day_difference > 0:
            self.TBB_week_points += tbb_day_difference
            self.TBB_month_points += tbb_day_difference
            self.TBB_year_points += tbb_day_difference
            self.TBB_alltime_points += tbb_day_difference
        self.TBB_previous_day_points = self.TBB_day_points
        
        # Calculate Fiber_day_points
        fiber_day_difference = self.Fiber_day_points - self.Fiber_previous_day_points
        if fiber_day_difference > 0:
            self.Fiber_week_points += fiber_day_difference
            self.Fiber_month_points += fiber_day_difference
            self.Fiber_year_points += fiber_day_difference
            self.Fiber_alltime_points += fiber_day_difference
        self.Fiber_previous_day_points = self.Fiber_day_points
        
        # Calculate Densification_day_points
        densification_day_difference = self.Densification_day_points - self.Densification_previous_day_points
        if densification_day_difference > 0:
            self.Densification_week_points += densification_day_difference
            self.Densification_month_points += densification_day_difference
            self.Densification_year_points += densification_day_difference
            self.Densification_alltime_points += densification_day_difference
        self.Densification_previous_day_points = self.Densification_day_points
        
        super(Profile, self).save(*args, **kwargs)

class Competition(models.Model):
    user = models.ForeignKey(User, related_name='comps', on_delete=models.CASCADE, blank=True, null=True)
    prize = models.TextField()    
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prize

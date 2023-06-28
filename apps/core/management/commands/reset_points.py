import schedule
import time
from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.core.models import Profile

class Command(BaseCommand):
    help = 'Reset player points to 0 at midnight'

    def reset_day_points(self):
        # Reset the day points of all profiles to 0
        Profile.objects.update(day_points=0)

    def handle(self, *args, **options):
        # Schedule the reset_day_points function to run at midnight every day
        schedule.every().day.at('00:00').do(self.reset_day_points)

        # Run the schedule continuously
        while True:
            schedule.run_pending()
            time.sleep(1)

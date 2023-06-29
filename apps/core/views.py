import warnings
from urllib import *
from django.shortcuts import *

from django.shortcuts import *
from django.http import *
from django.core.mail import *
from django.contrib.auth import *
from django.template.loader import *
from textwrap import *
from django.views.decorators.csrf import *
from django.db.models import * 
from django.contrib.auth.decorators import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import *


# Home
@login_required
def home(request):      
    profiles = Profile.objects.filter(active=True)

    profiles = Profile.objects.order_by('-day_points')  # Sort by points in descending order

    context = {
        'profiles': profiles,
    }

    return render(request, 'core/home.html', context)  

# def reset_day_points():
#     # Reset the day points of all profiles to 0
#     Profile.objects.update(day_points=0)



@login_required
def week(request):      
    profiles = Profile.objects.filter(active=True)

    profiles = Profile.objects.order_by('-week_points')  # Sort by points in descending order

    context = {
        'profiles': profiles,
    }
    return render(request, 'hof/week.html', context)    


@login_required
def month(request):      
    profiles = Profile.objects.filter(active=True)

    profiles = Profile.objects.order_by('-month_points')  # Sort by points in descending order

    context = {
        'profiles': profiles,
    }
    return render(request, 'hof/month.html', context)    

@login_required
def year(request):      
    profiles = Profile.objects.filter(active=True)

    profiles = Profile.objects.order_by('-year_points')  # Sort by points in descending order

    context = {
        'profiles': profiles,
    }
    return render(request, 'hof/year.html', context)    

@login_required
def alltime(request):      
    profiles = Profile.objects.filter(active=True)

    profiles = Profile.objects.order_by('-alltime_points')  # Sort by points in descending order

    context = {
        'profiles': profiles,
    }
    return render(request, 'hof/alltime.html', context)    








# def contact(request):
#     if request.method=='POST' and 'contact' in request.POST:
#         navn = request.POST.get('navn')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

#         data = {
#             'navn': navn,
#             'email': email,
#             'message': message,
#         }
#         message = dedent('''
#         Fra: {}

#         Navn: {}

#         Beskjed: {}
#         ''').format(data['email'], data['navn'], data['message'], )
#         send_mail('Epost fra portfolio', message, '', ['sabertoothtri@gmail.com'])
#         return redirect('/')
#     return render(request, 'pages/contact.html')  
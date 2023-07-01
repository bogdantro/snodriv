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
    profiles = Profile.objects.filter(active=True).order_by('-day_points')

    context = {
        'profiles': profiles,
    }

    return render(request, 'core/home.html', context)  

# def reset_day_points():
#     # Reset the day points of all profiles to 0
#     Profile.objects.update(day_points=0)



@login_required
def week(request):      
    profiles = Profile.objects.filter(active=True).order_by('-week_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'hof/week.html', context)    


@login_required
def month(request):      
    profiles = Profile.objects.filter(active=True).order_by('-month_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'hof/month.html', context)    

@login_required
def year(request):      
    profiles = Profile.objects.filter(active=True).order_by('-year_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'hof/year.html', context)    

@login_required
def alltime(request):      
    profiles = Profile.objects.filter(active=True).order_by('-alltime_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'hof/alltime.html', context)    


@login_required
def comp(request):
    profiles = Profile.objects.filter(active=True).order_by('-comp_points')

    comp = Competition.objects.filter(active=True)

    context = {
        'profiles': profiles,
        'comp': comp,
    }
    return render(request, 'comp/comp.html', context)  




@login_required
def tbb_day(request):
    profiles = Profile.objects.filter(TBB=True).order_by('-TBB_day_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'tbb/tbb-day.html', context)  

@login_required
def tbb_week(request):
    profiles = Profile.objects.filter(TBB=True).order_by('-TBB_week_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'tbb/tbb-week.html', context)  

@login_required
def tbb_month(request):
    profiles = Profile.objects.filter(TBB=True).order_by('-TBB_month_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'tbb/tbb-month.html', context)  

@login_required
def tbb_year(request):
    profiles = Profile.objects.filter(TBB=True).order_by('-TBB_year_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'tbb/tbb-year.html', context)  

@login_required
def tbb_alltime(request):
    profiles = Profile.objects.filter(TBB=True).order_by('-TBB_alltime_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'tbb/tbb-alltime.html', context)  




@login_required
def fiber_day(request):
    profiles = Profile.objects.filter(Fiber=True).order_by('-Fiber_day_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'fiber/fiber-day.html', context)  


@login_required
def fiber_week(request):
    profiles = Profile.objects.filter(Fiber=True).order_by('-Fiber_week_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'fiber/fiber-week.html', context)  


@login_required
def fiber_month(request):
    profiles = Profile.objects.filter(Fiber=True).order_by('-Fiber_month_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'fiber/fiber-month.html', context)  


@login_required
def fiber_year(request):
    profiles = Profile.objects.filter(Fiber=True).order_by('-Fiber_year_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'fiber/fiber-year.html', context)  


@login_required
def fiber_alltime(request):
    profiles = Profile.objects.filter(Fiber=True).order_by('-Fiber_alltime_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'fiber/fiber-alltime.html', context)  



@login_required
def dens_day(request):
    profiles = Profile.objects.filter(Densification=True).order_by('-Densification_day_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'dens/dens-day.html', context)  
@login_required
def dens_week(request):
    profiles = Profile.objects.filter(Densification=True).order_by('-Densification_week_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'dens/dens-week.html', context)  
@login_required
def dens_month(request):
    profiles = Profile.objects.filter(Densification=True).order_by('-Densification_month_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'dens/dens-month.html', context)  
@login_required
def dens_year(request):
    profiles = Profile.objects.filter(Densification=True).order_by('-Densification_year_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'dens/dens-year.html', context)  
@login_required
def dens_alltime(request):
    profiles = Profile.objects.filter(Densification=True).order_by('-Densification_alltime_points')

    context = {
        'profiles': profiles,
    }
    return render(request, 'dens/dens-alltime.html', context)  






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
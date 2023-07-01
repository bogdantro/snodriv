from django.urls import path
from apps.core.views import *
from django.conf.urls.static import *
from django.conf import *
from django.contrib import admin
from django.contrib.auth import views

from apps.core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from apps.userprofile.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Hall of Fame
    path('', home, name='home'),
    path('hall-of-fame-uke/', week, name='week'),
    path('hall-of-fame-maaned/', month, name='month'),
    path('hall-of-fame-aar/', year, name='year'),
    path('hall-of-fame-alltime/', alltime, name='alltime'),

    # Comp
    path('competition/', comp, name='comp'),

    # TBB
    path('cat-tbb-day/', tbb_day, name='tbb_day'),
    path('cat-tbb-week/', tbb_week, name='tbb_week'),
    path('cat-tbb-month/', tbb_month, name='tbb_month'),
    path('cat-tbb-year/', tbb_year, name='tbb_year'),
    path('cat-tbb-alltime/', tbb_alltime, name='tbb_alltime'),

    # Fiber
    path('cat-fiber-day/', fiber_day, name='fiber_day'),
    path('cat-fiber-week/', fiber_week, name='fiber_week'),
    path('cat-fiber-month/', fiber_month, name='fiber_month'),
    path('cat-fiber-year/', fiber_year, name='fiber_year'),
    path('cat-fiber-alltime/', fiber_alltime, name='fiber_alltime'),

    # Densification
    path('cat-dens-day/', dens_day, name='dens_day'),
    path('cat-dens-week/', dens_week, name='dens_week'),
    path('cat-dens-month/', dens_month, name='dens_month'),
    path('cat-dens-year/', dens_year, name='dens_year'),
    path('cat-dens-alltime/', dens_alltime, name='dens_alltime'),


    # Auth
    path('logg-inn/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('snodrivlagbruker123456/', signup, name='signup'),
    path('logg-ut/', views.LogoutView.as_view(), name='logout'),
    path('min-bruker/', myaccount, name='myaccount'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
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

    # Auth
    path('logg-inn/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('snodrivlagbruker123456/', signup, name='signup'),
    path('logg-ut/', views.LogoutView.as_view(), name='logout'),
    path('min-bruker/', myaccount, name='myaccount'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
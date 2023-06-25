from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserprofileForm
from django.contrib.auth import login
from textwrap import dedent
from django.core.mail import send_mail, BadHeaderError


@login_required
def myaccount(request):

    return render(request, 'core/myaccount.html')



def signup(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        userprofileform = UserprofileForm(request.POST)

        if form.is_valid() and userprofileform.is_valid():
            user = form.save()

            userprofile = userprofileform.save(commit=False)
            userprofile.user = user
            userprofile.save()

            login(request, user)

            return redirect('/min-bruker/')
    else:
        form = SignUpForm()
        userprofileform = UserprofileForm()

    return render(request, 'core/signup.html', {'form': form, 'userprofileform': userprofileform})    

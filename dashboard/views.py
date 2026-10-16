from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
@login_required
@never_cache
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')
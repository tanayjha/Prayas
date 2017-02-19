from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.contrib.auth import logout

@require_http_methods(['GET', 'POST'])
def handleLogin(request):
    if request.user.is_authenticated():
        return redirect('add-student')
    f = LoginForm(request.POST or None)
    # forgot = ForgetForm(request.POST or None)
    if request.method=='POST':
        nexturl = request.POST.get('next')
    if f.is_valid():
    	user = f.get_user()
    	login(request, user)
    data = {'form':f}
    return render(request,'main/login.html',data)

@require_http_methods(['GET', 'POST'])
@login_required
def handleLogout(request):	 
	logout(request)
	f = LoginForm(request.POST or None)
	data = {'form':f}
	return render(request, 'main/login.html', data)

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginForm
from ecoapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def Register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		name = request.POST.get('name')
		surname = request.POST.get('surname')
		tel = request.POST.get('tel')
		
		if form.is_valid():
			user = form.save()
			Customer.objects.create(user=user,name=name,surname=surname,tel=tel)
			
			return redirect('login')
	context = {
	'form':form,
	}
	return render(request, 'authT/register.html', context)
def LoginForm(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password = password)
		if user is not None:
			login(request, user)
			return redirect('cabinet')

	context = {}
	
	return render(request, 'authT/login.html', context)
def logoutUser(request):
	logout(request)
	return redirect('login')
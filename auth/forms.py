from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ecoapp.models import *
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields=['username','email','password1','password2']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'surname', 'tel', 'image']
        labels = {
            'name': 'First Name',
            'surname': 'Last Name',
            'tel': 'Phone Number',
            'image': 'Profile Image',
        }


class LoginForm(UserCreationForm):
	class Meta:
		model = User
		fields=['username', 'email']
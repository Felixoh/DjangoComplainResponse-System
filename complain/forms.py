from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Complain,Response

class CreateUser(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
			'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'EmailHere'}),
			'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
			'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'PasswordConfirmation'}),
		}
class ComplainForm(forms.ModelForm): 
	class Meta:
		model = Complain
		fields = ['location','complains','comment']
		
		#styling widgets with bootstrap CSS
		widgets = {
		'location':forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),
		'complains':forms.Select(attrs={'class':'form-control'}),
		'comment':forms.TextInput(attrs={'class':'form-control'}),
		}

from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(AuthenticationForm):
	"""ログオンフォーム"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['placeholder'] = field.label

User = get_user_model()

"""account register form"""
class RegistrationForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = (
			'username', 'email',
			'password1', 'password2',
		)
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'


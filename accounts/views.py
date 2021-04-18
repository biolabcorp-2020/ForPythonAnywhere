from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from .forms import LoginForm
from django.views import generic
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from .forms import RegistrationForm


class Login(LoginView):
	"""ログインページ"""
	form_class = LoginForm
	template_name = 'login.html'


class Top(LoginRequiredMixin, generic.TemplateView):
	""" トップページ """
	template_name = 'top.html'
	redirect_field_name = 'redirect_to'


class Logout(LoginRequiredMixin, LogoutView):
	"""ログアウトページ"""
	template_name = 'logout.html'

User = get_user_model()

""" account register page """
class Registration(generic.CreateView):
	model = User
	template_name = 'registration.html'
	form_class = RegistrationForm
	success_url = '/registration/complete'

""" account registration complete """
class RegistrationComp(generic.TemplateView):
	template_name = 'registration_complete.html'



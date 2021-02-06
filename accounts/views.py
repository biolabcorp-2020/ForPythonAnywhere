from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from .forms import LoginForm
from django.views import generic
from django.contrib.auth.decorators import login_required


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


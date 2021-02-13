from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('', views.Login.as_view(), name='login'),
	path('accounts/profile/', views.Top.as_view(), name='profile'),
	path('logout/', views.Logout.as_view(), name='logout'),
]


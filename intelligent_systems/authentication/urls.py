from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('sign-up', views.signup, name='signup'),
    path('sign-in', views.signin, name='signin'),
    path('', lambda request: redirect('signin')),
    path('logout', views.logout_user, name='logout'),
    
]

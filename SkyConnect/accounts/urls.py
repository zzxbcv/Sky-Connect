from django.urls import path
from .views import login_view, signup_view, settings_view, profile_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('settings/', settings_view, name='settings'),
    path('profile/', profile_view, name='profile'),
]
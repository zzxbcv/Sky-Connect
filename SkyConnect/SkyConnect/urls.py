"""
URL configuration for SkyConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
# For more information on this file, see
# https://docs.djangoproject.com/en/5.2/topics/settings/
"""

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # dashboard
    path('dashboard/', include('dashboard.urls')),

    # Auth (login, signup)
    path('', include('accounts.urls')),

    # Messages app (Student 3)
    path('messages/', include('user_messages.urls')),

    # Teams app (Student 1) — add when ready
    # path('teams/', include('teams.urls')),

    # Organisation app (Student 2) — add when ready
    # path('organisation/', include('organisation.urls')),

    # Schedule app (Student 4) — add when ready
    # path('schedule/', include('schedule.urls')),

    # Report app (Student 5) — add when ready
    # path('report/', include('report.urls')),

    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
]
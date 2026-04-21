"""
URL configuration for SkyConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

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

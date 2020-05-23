"""StudyManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
# from django.contrib.auth import views as auth.views
from django.views.generic.base import TemplateView
from documents import views
from registration import views as registration_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('upload/', views.upload),
    path('documents/', views.doclist),
   
    # This path is needed, to delete the file (compares primary key of file)
    path('documents/<int:pk>', views.deletedoc, name='deletedoc'),
   
    # include the auth app at accounts/ - standard provided by django
    path('registration/', registration_views.signup, name='signup'),
    path('registration/', include('django.contrib.auth.urls')),
    # change password
    path('password_change/', registration_views.password_change, name='password_change'),
]

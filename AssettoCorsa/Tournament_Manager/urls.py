"""
URL configuration for Tournament_Manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

def views_for(resource : str):
    '''
    Return the result of `django.urls.include` with a path to the specific views package in this app.

    :resource: The name of the file in the views folder

    Just to make it easier if the name of the app 'Tournament_Manager_App' ever changes.
    '''
    return include(f'Tournament_Manager_App.views.{resource}')

urlpatterns = [
    path('', views_for('index'), name='index'),
    path('admin/', admin.site.urls),
    # path('accounts/'),
    path('tournaments/', views_for('tournaments'), name='tournaments'),
    # path('cars/')
]

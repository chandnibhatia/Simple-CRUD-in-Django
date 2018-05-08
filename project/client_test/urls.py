"""python_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'client_test'

urlpatterns = [
    path('', views.client_details, name='client_details'),
	path('user/new', views.user_new, name='user_new'),
    path('user/update', views.save_updated_user, name='save_updated_user'),
    path('user/get_updated_user/<int:pk>',views.get_updated_user, name='get_updated_user'),
    path('user/delete/<int:pk>', views.delete_user, name='delete_user'),
    path('ajax/getStates',views.get_states, name='get_states'),
    path('ajax/getCities',views.get_cities, name='get_cities'),
]

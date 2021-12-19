"""rk2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from parts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('me/', views.me, name="me"),
    path('part/', include([
        path('', views.read_part, name='read_part'),
        path('create/', views.create_part, name="create_part"),
        path('update/<int:part_id>/', views.update_part, name="update_part"),
        path('delete/<int:part_id>/', views.delete_part, name="delete_part"),
    ])),
    path('manufacturer/', include([
        path('', views.read_manufacturer, name='read_manufacturer'),
        path('create/', views.create_manufacturer, name="create_manufacturer"),
        path('update/<int:manufacturer_id>/',
             views.update_manufacturer, name="update_manufacturer"),
        path('delete/<int:manufacturer_id>/',
             views.delete_manufacturer, name="delete_manufacturer"),
    ])),
    path('report/', views.report, name="report"),
]

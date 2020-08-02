"""jiaofood URL Configuration

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
from django.urls import path,re_path
from foodapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    re_path(r'search/', views.search, name='search'),
    path('all/', views.RecipeList.as_view()),
    path('add/', views.RecipeCreate.as_view()),
    re_path(r'recipe/(?P<pk>\d+)', views.RecipeDetail.as_view()),
    path('error/', views.custom_404_view, name='error')
]


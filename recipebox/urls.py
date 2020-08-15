"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebox_app import views 



urlpatterns = [
path('', views.index, name="homepage"),
path('recipes/<int:recipe_id>/', views.recipe_detail_view),
path('author/<int:author_id>/', views.author_detail_view),
path('addauthor/', views.add_author),
path('addrecipe/', views.add_recipe),
path('login/', views.login_view, name="loginview"),
path('logout/', views.logout_view, name="logout"),
path('admin/', admin.site.urls),


]


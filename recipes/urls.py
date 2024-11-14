from django.contrib import admin
from django.urls import path
from recipes import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]

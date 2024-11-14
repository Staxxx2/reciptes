# myproject/recipes/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views  # Импортируем для Logout
from . import views  # Импортируем views из текущего приложения

urlpatterns = [
    # Главная страница сайта
    path('', views.home, name='home'),

    # Страница добавления рецепта
    path('add_recipe/', views.add_recipe, name='add_recipe'),

    # Страница регистрации пользователя
    path('register/', views.register, name='register'),

    # Страница входа
    path('login/', views.login_view, name='login'),

    # Страница выхода (используется LogoutView)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Детали рецепта по его ID
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),

    # Страница админского интерфейса для статистики или других функций
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]

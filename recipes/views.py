# myproject/recipes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Recipe, Category
from django.contrib.auth.models import User
from .forms import RecipeForm



# Главная страница, случайные рецепты
def home(request):
    recipes = Recipe.objects.all().order_by('?')[:5]  # 5 случайных рецептов
    return render(request, 'recipes/home.html', {'recipes': recipes})

# Страница одного рецепта
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Страница добавления рецепта
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Присваиваем автору рецепт
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

# Страница регистрации
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/register.html', {'form': form})

# Страница авторизации
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'recipes/login.html')

# Страница статистики для админов
def admin_dashboard(request):
    users = User.objects.all()
    user_stats = []

    for user in users:
        recipe_count = Recipe.objects.filter(author=user).count()
        user_stats.append({'user': user, 'recipe_count': recipe_count})

    return render(request, 'recipes/admin_dashboard.html', {'user_stats': user_stats})

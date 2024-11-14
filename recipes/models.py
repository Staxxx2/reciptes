from django.db import models
from django.contrib.auth.models import User

# Модель для категорий рецептов
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Модель для рецептов
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()  # Время приготовления в минутах
    image = models.ImageField(upload_to='recipes/images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Добавленное поле для времени создания

    def __str__(self):
        return self.title

# myproject/recipes/admin.py
from django.contrib import admin
from .models import Recipe, Category

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'cooking_time', 'created_at')
    search_fields = ('title', 'author__username', 'category__name')
    list_filter = ('author', 'category')

    # Настройки для удаления
    actions = ['delete_selected_recipes']
    
    def delete_selected_recipes(self, request, queryset):
        count, _ = queryset.delete()
        self.message_user(request, f"{count} рецептов было удалено")

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)

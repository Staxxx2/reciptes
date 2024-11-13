from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Административная панель
    path('', include('recipes.urls')),  # Подключение маршрутов из приложения recipes
]

# Добавляем маршруты для работы с медиафайлами в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

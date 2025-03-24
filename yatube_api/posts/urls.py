from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Добавьте другие маршруты, если они есть
]

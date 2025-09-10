from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='books.index'),
    path('<int:isbn>/', views.show, name='books.show'),
]
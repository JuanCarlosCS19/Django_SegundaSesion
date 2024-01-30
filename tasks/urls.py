from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks),
    path('new/', views.create_task, name='create_task')
]
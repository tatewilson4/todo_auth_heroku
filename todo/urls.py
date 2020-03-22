from django.urls import path, include
from django.conf import settings
from . import views




urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('view/<int:pk>', views.todo_view, name='todo_detail'),
    path('new/', views.todo_create, name='todo_new'),
    path('edit/<int:pk>', views.todo_update, name='todo_edit'),
    path('delete/<int:pk>', views.todo_delete, name='todo_delete'),

]

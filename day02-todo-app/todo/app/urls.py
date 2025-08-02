from django.urls import path
from .import views 

urlpatterns = [
  path('', views.ToDoListView.as_view(), name='todo_list'),
  path('add/', views.ToDoCreateView.as_view(), name = 'todo_create'),
  path('<int:pk>/edit/', views.ToDoUpdateView.as_view(), name = 'todo_update'),
  path('<int:pk>/delete/', views.ToDoDeleteView.as_view(), name = 'todo_confirm_delete'),
]
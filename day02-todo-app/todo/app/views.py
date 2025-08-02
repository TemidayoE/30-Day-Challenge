from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import ToDo

# Create your views here.
class ToDoListView(ListView):
  model = ToDo
  template_name = "app/todo_list.html"

class ToDoCreateView(CreateView):
  model = ToDo
  fields = ["title", "description", "status"]
  template_name = "app/todo_form.html"
  success_url = reverse_lazy("todo_list")

class ToDoUpdateView(UpdateView):
  model = ToDo
  fields = ["title", "description", "status"]
  template_name = "app/todo_form.html"
  success_url = reverse_lazy("todo_list")

class ToDoDeleteView(DeleteView):
  model = ToDo
  template_name = "app/todo_confirm_delete.html"
  success_url = reverse_lazy("todo_list")

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.forms import ModelForm
from todo.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['item']
        exclude = ['user']

def base(request, template_name='base.html'):
    return render(request, template_name)


def home(request, template_name='home.html'):
    user = request.user
    todo = Todo.objects.filter(user=user)
    data = {}
    data['object_list'] = todo
    return render(request, template_name, data)

def todo_view(request, pk, template_name='todo_detail.html'):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, template_name, {'object':todo})

def todo_create(request, template_name="todo_form.html"):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

def todo_update(request, pk, template_name='todo_form.html'):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

def todo_delete(request, pk, template_name='todo_confirm_delete.html'):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, template_name, {'object':todo})

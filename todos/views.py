from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()

    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'form': form,
        'total': todos.count(),
        'done': todos.filter(completed=True).count(),
    }
    return render(request, 'todos/index.html', context)

def toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')

def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit.html', {'form': form, 'todo': todo})

def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('index')
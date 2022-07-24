from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm
# Create your views here.


def create(request):
    message = ''
    form = TodoForm()

    if request.method == 'POST':
        message = '資料輸入錯誤'
        try:
            form = TodoForm(request.POST)
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            return redirect('todo')

        except Exception as e:
            print(e)

    return render(request, './todo/create.html', {'form': form, 'message': message})


def view(request, id):
    todo = get_object_or_404(Todo, id=id)

    return render(request, './todo/view.html', {'todo': todo})


def todo(request):

    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
        print(todos)

    return render(request, './todo/todo.html', {'todos': todos})

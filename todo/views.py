from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView

from .models import *
from .forms import TodosForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def do_edit(request, pk):
    do = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodosForm(request.POST, instance=do)
        if form.is_valid():
            do = form.save(commit=False)
            do.author = request.user
            # return HttpResponse(do)
            do.save()
            return redirect('/', pk=do.pk)
    else:
        form = TodosForm(instance=do)
    return render(request, 'edit_do.html', {'form': form})

# @login_required()
# class EditTodoView(UpdateView):
#     model = Todo
#     template_name = 'edit_do.html'
#     fields = ['title', 'content', 'srok']
    # widgets = {
    #     # 'author': forms.TextInput(attrs={'class': 'form-control'}),
    #     'title': forms.TextInput(
    #         attrs={'class': 'form-control m-2'}
    #     ),
    #     'content': forms.TextInput(
    #         attrs={'class': 'form-control m-2'}
    #     ),
    #     'srok': forms.DateInput(
    #         attrs={'class': 'form-control m-2 col-sm-3'}
    #     ),
    # }

    # def get_absolute_url(self):
    #     return redirect('/')

    # def post(self, request, pk):
    #     if request.method == 'POST':
    #         form = TodosForm(request.POST)
    #
    #         if form.is_valid():
    #             list1 = form.save(commit=False)
    #             list1.author = request.user
    #             list1.save()
    #         # return HttpResponse(form)
    #         return redirect('/')


def index(request):
    delas = Todo.objects.filter(author=request.user.pk)
    return render(request, 'index.html', {'delas': delas})


def all_news(request):
    delas = Todo.objects.all()
    return render(request, 'all_does.html', {'delas': delas})


def delete_all(request):
    all_delas = Todo.objects.filter(author=request.user.pk)
    all_delas.delete()
    return redirect('.')


def author(request, user_id):
    delas = Todo.objects.filter(author=user_id)
    author_name = User.objects.get(pk=user_id)
    return render(request, 'author.html', {'delas': delas, 'author_name': author_name})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required()
def create(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            list1 = form.save(commit=False)
            list1.author = request.user
            list1.save()
        else:
            errors = [i for i in form.errors]

            # return redirect(request.META.get('HTTP_REFERER', '/'))
            return render(request, 'create_do.html', {'form': form, 'errors': errors})

        # form.save(commit=False)

        # return HttpResponse(form.is_valid())
    else:
        form = TodosForm()
        return render(request, 'create_do.html', {'form': form})
    return redirect('/')


@login_required()
def delety(request, id):
    post = Todo.objects.get(id=id)
    # return HttpResponse(post)
    post.delete()
    return redirect('/')



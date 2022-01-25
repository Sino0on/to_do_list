from django import forms
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import *
from .forms import TodosForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

# @login_required()
class EditTodoView(UpdateView):
    model = Todo
    template_name = 'edit_do.html'
    fields = ['title', 'content', 'srok']
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
    delas = Todo.objects.all()
    return render(request, 'index.html', {'delas': delas})


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



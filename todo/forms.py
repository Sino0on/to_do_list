from django import forms
from .models import *


class TodosForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'content', 'srok']
        widgets = {
            # 'author': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(
                attrs={'class': 'form-control m-2'}
            ),
            'content': forms.TextInput(
                attrs={'class': 'form-control m-2'}
            ),
            'srok': forms.DateInput(
                attrs={'class': 'form-control m-2 col-sm-3'}
            ),
        }


from django.conf import settings
from django.db import models
from django.db.models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class Todo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    srok = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'
        ordering = ['-created']

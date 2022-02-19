from email import contentmanager
from multiprocessing import managers
from operator import mod
from pyexpat import model
from statistics import mode
from turtle import title
from venv import create
from django.db import models
from django.contrib.auth.models import User
from platformdirs import user_cache_dir

class TodoListItem(models.Model):
    content=models.TextField()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content =models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

        
from email import contentmanager
from statistics import mode
from django.db import models

class TodoListItem(models.Model):
    content=models.TextField()
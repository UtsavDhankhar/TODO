from sqlite3 import complete_statement
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE , null = True , blank = True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True , blank=True)
    complete_date = models.DateField()
    create = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    
    


    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ['complete']

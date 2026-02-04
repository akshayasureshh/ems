from django.db import models
from .choices import FieldTypes

class DynamicForm(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FormField(models.Model):
    form = models.ForeignKey(DynamicForm, related_name='fields', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    field_type = models.CharField(max_length=20, choices=FieldTypes.choices)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']


class Employee(models.Model):
    form = models.ForeignKey(DynamicForm, on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

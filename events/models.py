from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=100, default='')
    desc = models.TextField(blank=True, null=True, default='')
    time_creation = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

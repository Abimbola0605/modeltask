from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,)

    created_date = models.DateField()
    published_date = models.DateField
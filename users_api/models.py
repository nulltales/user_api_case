from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    birthday = models.DateField(null=True)

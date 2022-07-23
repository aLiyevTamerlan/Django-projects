from django.db import models

# Create your models here.
class Charity(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    money = models.IntegerField()
    def __str__(self):
        return self.username
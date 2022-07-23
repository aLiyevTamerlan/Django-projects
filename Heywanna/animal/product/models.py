from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Product(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True, verbose_name='Şəkil əlavə etmək:')
    product_name = models.CharField(max_length=150)
    product_content=models.CharField(max_length=150)
    animal_type = models.CharField(max_length=50,null=True)
    animal_gender = models.CharField(max_length=100,null=True)
    animal_category=models.CharField(max_length=150,null=True)
    date_added = models.DateTimeField(default=now)
    def __str__(self):
        return self.product_name

class Comment(models.Model):
    comment=models.TextField()
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_to',blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,related_name='replies',blank=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:20]

class Notice(models.Model):
    gonderen=models.ForeignKey(User, on_delete=models.CASCADE,related_name='gonderen')
    qebul_eden=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    baxilma=models.BooleanField(default=False,null=True,blank=True)
    tesdiq=models.BooleanField(default=None,null=True,blank=True)
    image = models.FileField(blank=True, null=True, verbose_name='Şəkil əlavə etmək:')
    timestamp = models.DateTimeField(default=now)

class Own(models.Model):
    sahiblenen=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sahiblenen')
    mehsul_sahibi=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
class Contact(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    email = models.EmailField(max_length = 254)
    message=models.CharField(max_length=250)
#& c:/Users/TAMERLAN/Desktop/myenv/Scripts/Activate.ps1
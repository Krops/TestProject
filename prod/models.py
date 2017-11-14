from django.db import models
from django.core.urlresolvers import reverse

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[str(self.slug)])

class User(models.Model):
    name = models.SlugField(unique=True)
    password = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    avatar_url = models.URLField()
    bio = models.TextField()
    rate = models.IntegerField(default=0)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user', args=[str(self.slug)])

class Comment(models.Model):
    time_post = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='dron')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    message = models.TextField()
    rate = models.IntegerField(default=0)

class Vote(models.Model):
    product = models.ForeignKey(Product,default=1)
    author = models.ForeignKey(User,default=1)
    rate = models.BooleanField('Liked')
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from django_prices.models import PriceField


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = PriceField('Price', currency='USD', max_digits=12, decimal_places=2)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    cover = ResizedImageField(size=[400, 400], upload_to='assets/images', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[str(self.slug)])


class User(AbstractUser):
    cover = ResizedImageField(size=[100, 100], upload_to='assets/images', null=True, blank=True)
    bio = models.TextField()
    rate = models.IntegerField(default=0)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user', args=[str(self.slug)])


class Comment(models.Model):
    time_post = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='dron')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    form_message = models.TextField()
    rate = models.IntegerField(default=0)


class Vote(models.Model):
    product = models.ForeignKey(Product, default=1)
    author = models.ForeignKey(User, default=1)
    rate = models.BooleanField('Liked')

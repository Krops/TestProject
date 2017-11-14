from django.contrib import admin
from prod.models import Product, Comment, User


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('slug', {'fields': ['slug']}),
        ('description', {'fields': ['description']}),
        ('price', {'fields': ['price']}),
        ('rate', {'fields': ['rate']}),
    ]
    list_display = ('name', 'slug', 'description', 'price', 'rate')
    search_fields = ["name"]


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('user', {'fields': ['user']}),
        ('product', {'fields': ['product']}),
        ('message', {'fields': ['message']}),

    ]
    list_display = ('user', 'message')
    search_fields = ["message"]

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('email', {'fields': ['email']}),
        ('bio', {'fields': ['bio']}),

    ]
    list_display = ('name', 'email')
    search_fields = ["name"]


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
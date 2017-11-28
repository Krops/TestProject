from django.contrib import admin
from prod.models import Product, Comment, User, Vote


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('slug', {'fields': ['slug']}),
        ('description', {'fields': ['description']}),
        ('price', {'fields': ['price']}),
        ('rate', {'fields': ['rate']}),
        ('cover', {'fields': ['cover']}),
    ]
    list_display = ('name', 'slug', 'description', 'price', 'rate')
    search_fields = ["name"]


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('user', {'fields': ['user']}),
        ('product', {'fields': ['product']}),
        ('form_message', {'fields': ['form_message']}),

    ]
    list_display = ('user', 'form_message')
    search_fields = ["form_message"]


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('username', {'fields': ['username']}),
        ('email', {'fields': ['email']}),
        ('bio', {'fields': ['bio']}),
        ('cover', {'fields': ['cover']}),

    ]
    list_display = ('username', 'email')
    search_fields = ["username"]


class VoteAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'rate')


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Vote, VoteAdmin)

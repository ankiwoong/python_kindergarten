from django.contrib import admin
from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)

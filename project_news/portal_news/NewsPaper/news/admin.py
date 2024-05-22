from django.contrib import admin
from .models import *

class CategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = (CategoryInline, )


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
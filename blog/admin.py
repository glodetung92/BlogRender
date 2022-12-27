from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'slug', 'author', 'status', 'created_on',)
    model = Post
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)

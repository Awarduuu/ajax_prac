from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'title',
        'content',
        'view_count',
        'created_at',
    )

    search_fields =(
        'title',
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =(
        'id', 
        'content',
        'writer',
        'created_at',
        'deleted',
    )
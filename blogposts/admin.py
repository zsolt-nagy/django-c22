from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'text', 'publish_date')

admin.site.register(Post, PostAdmin)

from django.contrib import admin
from myblog.models import Blog, Tag, Post

# Register your models here.

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Post)

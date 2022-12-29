from django.contrib import admin
from .models import Post
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Post, MyModelAdmin)
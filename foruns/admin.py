from django.contrib import admin

# Register your models here.

from .models import AutorPost, ForumPost, ForumPostComment, GeneroForum

admin.site.register(ForumPost)
admin.site.register(ForumPostComment)
admin.site.register(AutorPost)
admin.site.register(GeneroForum)
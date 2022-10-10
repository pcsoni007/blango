from django.contrib import admin
from .models import Tag, Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
  prepulated_fields = { "slug": ("title",  ) }
  list_display = ["title", "published_at","author"]


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

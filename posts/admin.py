from django.contrib import admin
from posts.models import Post, Category, Tag
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "rate", "created_at", "updated_at"]
    list_editable = ("category",)
admin.site.register(Category)
admin.site.register(Tag)
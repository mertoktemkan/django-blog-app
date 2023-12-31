from django.contrib import admin
from .models import Article,Comment
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_time"]
    list_display_links = ["title"]
    search_fields = ["title"]
    list_filter = ["created_time"]
    class Meta:
        model = Article

admin.site.register(Comment)
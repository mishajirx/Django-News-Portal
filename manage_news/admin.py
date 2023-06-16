from django.contrib import admin
from .models import News, Tag


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']

    class Meta:
        model = Tag


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_urgent', 'category', 'get_tags']
    search_fields = ['title', 'content']
    list_filter = ['author', 'category', 'tags']

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
admin.site.register(Tag, TagAdmin)

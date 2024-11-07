from django.contrib import admin
from Blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'image']
    list_display = ('title', 'content', 'pub_date',)
    list_filter = ('pub_date',)
    search_fields = ('title',)


admin.site.register(Blog, BlogAdmin)

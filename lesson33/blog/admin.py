from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title')
    list_display_links = ('slug',)
    ordering = ('title',)
    search_fields = ('title',) # LIKE '%word%'
    # list_filter = ('status')


admin.site.register(Post, PostAdmin)

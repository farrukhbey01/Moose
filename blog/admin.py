from django.contrib import admin
from .models import Post, Contact,Comments,Category


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ['id', 'full_name']


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published','view_count')
    list_display_links = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Category)

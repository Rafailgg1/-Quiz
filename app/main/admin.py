from django.contrib import admin


from .models import (Topic, Application, Post, Comment, Tag)




admin.site.register(Application)
# @admin.register(Application)
# class AplicationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'topic', 'user', 'application', 'created_at', 'updated_at')
#     list_display_links = ('id','topic', 'user', 'application')
#     search_fields = ('user__username','content', 'topic__title', 'tags__title')
#     list_filter = ('topic', 'tags','created_at', 'updated_at')
#     readonly_fields = ('created_at', 'updated_at')
#     filter_horizontal = ('tags',)

admin.site.register(Post)
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'topic', 'user', 'application', 'created_at', 'updated_at')
#     list_display_links = ('id','topic', 'user', 'application')
#     search_fields = ('user__username','content', 'topic__title', 'tags__title')
#     list_filter = ('topic', 'tags','created_at', 'updated_at')
#     readonly_fields = ('created_at', 'updated_at')
#     filter_horizontal = ('tags',)

admin.site.register(Comment)
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'topic', 'user', 'application', 'created_at', 'updated_at')
#     list_display_links = ('id','topic', 'user', 'application')
#     search_fields = ('user__username','content', 'topic__title', 'tags__title')
#     list_filter = ('topic', 'tags','created_at', 'updated_at')
#     readonly_fields = ('created_at', 'updated_at')
#     filter_horizontal = ('tags',)

admin.site.register(Topic)
# @admin.register(Topic)
# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('id', 'topic', 'user', 'application', 'created_at', 'updated_at')
#     list_display_links = ('id','topic', 'user', 'application')
#     search_fields = ('user__username','content', 'topic__title', 'tags__title')
#     list_filter = ('topic', 'tags','created_at', 'updated_at')
#     readonly_fields = ('created_at', 'updated_at')
#     filter_horizontal = ('tags',)


admin.site.register(Tag)
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('id', 'topic', 'user', 'application', 'created_at', 'updated_at')
#     list_display_links = ('id','topic', 'user', 'application')
#     search_fields = ('user__username','content', 'topic__title', 'tags__title')


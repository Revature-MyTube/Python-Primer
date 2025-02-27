from django.contrib import admin
from . import models


class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'views')
    list_filter = ('name', 'views')
    
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'owner')
    list_filter = ('name', 'views', 'owner')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('video', 'author', 'created_at')
    list_filter = ('video', 'author', 'created_at')

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'created_at')
    list_filter = ('name', 'about', 'created_at')


admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.Channel, ChannelAdmin)
admin.site.register(models.Playlist, PlaylistAdmin)
admin.site.register(models.Comment, CommentAdmin)

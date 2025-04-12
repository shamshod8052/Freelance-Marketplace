from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'order', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('message', 'sender__username', 'receiver__username')
    readonly_fields = ('timestamp',)

    fieldsets = (
        (None, {
            'fields': ('sender', 'receiver', 'order', 'service', 'message', 'status')
        }),
        ('Media', {
            'fields': ('image', 'video'),
        }),
        ('Timestamps', {
            'fields': ('timestamp',),
        }),
    )

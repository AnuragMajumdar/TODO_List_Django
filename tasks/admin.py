from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'user', 'created_at')
    list_filter = ('status', 'user')
    search_fields = ('name', 'user__username')
    ordering = ('-created_at',)
    
    def get_queryset(self, request):
        # Override this method to ensure all tasks are visible, regardless of the user
        return super().get_queryset(request)

    def has_change_permission(self, request, obj=None):
        # Allow editing all tasks
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting all tasks
        return True


from django.contrib import admin
from .models import Task, SubTask, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    list_filter = ('status', 'categories', 'deadline')
    search_fields = ('title', 'description')
    filter_horizontal = ('categories',)
    date_hierarchy = 'deadline'
    ordering = ['-created_at']


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'deadline')
    list_filter = ('status', 'task')
    search_fields = ('title', 'description')
    raw_id_fields = ('task',)
    ordering = ['-created_at']
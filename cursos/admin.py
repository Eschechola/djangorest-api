from django.contrib import admin

from .models import Course, Average


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'publishedAt', 'updatedAt', 'isActive')


@admin.register(Average)
class AverageAdmin(admin.ModelAdmin):
    list_display = ('courseId', 'name', 'email', 'average', 'publishedAt', 'updatedAt', 'isActive')


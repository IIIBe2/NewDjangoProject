from django.contrib import admin
from .models import Lesson, Product, UserCustom

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'author']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'link', 'secondsLesson']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['secondsLesson']
    list_editable = ['secondsLesson']

@admin.register(UserCustom)
class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['name', 'lessonID', 'TimeWatch', 'viewed']
from django.contrib import admin
from .models import Lesson, Product, UserCustom

class ModuleInline(admin.StackedInline):
    model = Lesson

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'author']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ModuleInline,]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'link', 'secondsLesson']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = [ 'secondsLesson']
    list_editable = ['secondsLesson']

@admin.register(UserCustom)
class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['name', 'lessonID', 'TimeWatch']
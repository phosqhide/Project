from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welkome to my courses"


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "students_qty")


class CoursesInline(admin.TabularInline):
    model = models.Course
    exclude = ("created_add",)
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_add")
    fieldsets = [
        (None, {"fields": ["title"]}),
        ('Dates', {
            "fields": ["created_add"],
            "classes": ["collapse"]
        }),
    ]
    inlines = [CoursesInline]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)

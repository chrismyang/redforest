

from telperion.models import School,Question,Essay,User
from django.contrib import admin

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class SchoolInline(admin.StackedInline):
    model=School
    extra = 3


class SchoolAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class UserAdmin(admin.ModelAdmin):
    inlines = [SchoolInline]


admin.site.register(School,SchoolAdmin)
admin.site.register(User)
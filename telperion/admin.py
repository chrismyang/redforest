

from telperion.models import School,Question,Essay
from django.contrib import admin

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class SchoolAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(School,SchoolAdmin)
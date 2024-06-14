# problems/admin.py
from django.contrib import admin
from .models import Problem, UserProblem, Theme

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'level')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('theme', 'level')
    search_fields = ('title','description')

class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)



admin.site.register(Problem, ProblemAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(UserProblem)

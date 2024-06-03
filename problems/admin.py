# problems/admin.py
from django.contrib import admin
from .models import Problem, UserProblem

admin.site.register(Problem)
admin.site.register(UserProblem)

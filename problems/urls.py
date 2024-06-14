# problems/urls.py
from django.urls import path
from . import views

app_name = 'problems'

urlpatterns = [
    path('problems/', views.problem_list, name='problem_list'),
    path('<int:pk>/', views.problem_detail, name='problem_detail'),
    path('problems/<slug>/', views.theme_list, name='problem-of-theme'),
]

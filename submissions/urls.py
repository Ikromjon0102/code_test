# problems/urls.py
from django.urls import path
from .views import submit_code, submission_result

app_name = 'submissions'
urlpatterns = [
    path('submit/<int:problem_id>/', submit_code, name='submit_code'),
    path('submission/<int:pk>/', submission_result, name='submission_result'),
]

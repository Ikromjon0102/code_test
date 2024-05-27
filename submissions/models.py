# submissions/models.py
from django.db import models
from django.contrib.auth import get_user_model
from problems.models import Problem

class Submission(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        # Yana boshqa tillarni qo'shishingiz mumkin
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    result = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='python')


    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"





# # submissions/models.py
# from django.db import models
# from problems.models import Problem
#
# class Submission(models.Model):
#     problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
#     code = models.TextField()
#     result = models.TextField()
#
#     def __str__(self):
#         return f'Submission for {self.problem.title} with result {self.result}'

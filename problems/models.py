from django.db import models

# class Problem(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     input_format = models.TextField()
#     output_format = models.TextField()
#     sample_input = models.TextField()
#     sample_output = models.TextField()
#     constraints = models.TextField()
#
#     def __str__(self):
#         return self.title


# problems/models.py
from django.db import models

from users.models import CustomUser


class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    input_format = models.TextField()
    output_format = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    test_cases = models.TextField()  # Test holatlarini saqlash uchun maydon

    def __str__(self):
        return self.title


class UserProblem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.problem} - {self.user}"
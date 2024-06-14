from django.db import models
from django.urls import reverse
from slugify import slugify

from users.models import CustomUser

class Theme(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Theme, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('problem-of-theme', args=[self.slug])

    def __str__(self):
        return self.name


class Problem(models.Model):
    class Level(models.TextChoices):
        EASY = 'easy', 'EASY'
        MEDIUM = 'medium', 'MEDIUM'
        HARD = 'hard', 'HARD'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(
        max_length=12,
        choices=Level.choices,
        default=Level.EASY
    )
    input_format = models.TextField()
    output_format = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    test_cases = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Problem, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserProblem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} -> {self.problem}'

    # def get_problems(request):
    #     problems = [i.title for i in Problem.objects.filter(user=request.user)]
    #     return problems

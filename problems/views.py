# problems/views.py
from django.shortcuts import render, get_object_or_404
from .models import Problem, Theme, UserProblem


def problem_list(request):
    problems = Problem.objects.all()
    query = request.GET.get('q')
    if query:
        problems = problems.filter(title__icontains=query)

    themes = Theme.objects.all()

    context = {'problems': problems, 'themes': themes}

    if request.user.is_authenticated:
        user_problems = [ i.problem.title for i in UserProblem.objects.filter(user=request.user)]
        context = {'problems': problems, 'themes': themes, 'user_problems': user_problems}
    return render(request, 'problems/problem_list.html', context)

def problem_detail(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    return render(request, 'problems/problem_detail.html', {'problem': problem})


def theme_list(request, slug):
    themes = Theme.objects.all()
    theme = Theme.objects.get(slug=slug)
    problems = Problem.objects.filter(theme=theme)
    context = {'theme': theme, 'problems': problems, 'themes': themes}

    if request.user.is_authenticated:
        user_problems = [i.problem.title for i in UserProblem.objects.filter(user=request.user)]
        context = {'theme': theme, 'problems': problems, 'themes': themes, 'user_problems': user_problems}

    return render(request, 'problems/theme.html', context)

# problems/views.py
# from django.shortcuts import render, get_object_or_404
# from .models import Problem

# def problem_list(request):
#     problems = Problem.objects.all()
#     return render(request, 'problems/problem_list.html', {'problems': problems})
#
# def problem_detail(request, pk):
#     problem = get_object_or_404(Problem, pk=pk)
#     return render(request, 'problems/problem_detail.html', {'problem': problem})

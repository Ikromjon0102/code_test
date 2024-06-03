from django import forms
from django.shortcuts import render

# Create your views here.
# submissions/views.py
from django.shortcuts import render, redirect
from .models import Submission
from problems.models import Problem
import subprocess

# def submit_code(request, problem_id):
#     problem = Problem.objects.get(pk=problem_id)
#     if request.method == "POST":
#         code = request.POST['code']
#         # Kodni bajarish va natijani olish
#         result = subprocess.run(['python3', '-c', code], capture_output=True, text=True)
#         output = result.stdout
#
#         submission = Submission.objects.create(
#             user=request.user,
#             problem=problem,
#             code=code,
#             result=output
#         )
#         return redirect('submission_result', pk=submission.pk)
#     return render(request, 'submissions/submit_code.html', {'problem': problem})
#
# def submission_result(request, pk):
#     submission = Submission.objects.get(pk=pk)
#     return render(request, 'submissions/submission_result.html', {'submission': submission})
#
#
# # Tekshirishni alohida funksiya qilib yaratish
# def run_code(code, input_data):
#     try:
#         # Kodni ishlatish
#         result = subprocess.run(['python3', '-c', code], input=input_data.encode(), capture_output=True, text=True, timeout=5)
#         return result.stdout.strip()
#     except subprocess.TimeoutExpired:
#         return "Execution Timed Out"


# submissions/views.py
import subprocess
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from problems.models import Problem
from .models import Submission


# @csrf_exempt
# def submit_code(request, problem_id):
#     problem = get_object_or_404(Problem, pk=problem_id)
#
#     if request.method == 'POST':
#         user_code = request.POST['code']
#         language = request.POST['language']
#         input_data = problem.sample_input
#         expected_output = problem.sample_output.strip()
#
#         print(user_code, language, input_data, expected_output)
#         # Yangi Submission yaratish
#         submission = Submission.objects.create(
#             user=request.user,
#             problem=problem,
#             code=user_code,
#             language=language,
#             result='',
#         )
#
#         # Kodni tekshirish
#         try:
#             # # Foydalanuvchi kodini faylga yozish
#             # with open('user_code.py', 'w') as code_file:
#             #     code_file.write(user_code)
#             #
#             # # Kodni ishga tushirish
#             # result = subprocess.run(
#             #     ['python', 'user_code.py'],
#             #     input=input_data,
#             #     text=True,
#             #     capture_output=True,
#             #     timeout=5  # 5 soniya ichida kod bajarilishi kerak
#             # )
#             #
#             # # Chiqarilgan natijani olish
#             if language == 'python':
#                 # Python kodini faylga yozish
#                 with open('user_code.py', 'w') as code_file:
#                     code_file.write(user_code)
#
#                 # Python interpreteri orqali ishga tushirish
#                 result = subprocess.run(
#                     ['python', 'user_code.py'],
#                     input=input_data,
#                     text=True,
#                     capture_output=True,
#                     timeout=5  # 5 soniya ichida kod bajarilishi kerak
#                 )
#
#             elif language == 'java':
#                 # Java kodini faylga yozish
#                 with open('User.java', 'w') as code_file:
#                     code_file.write(user_code)
#
#                 # Java kodini kompilyatsiya qilish
#                 subprocess.run(['javac', 'User.java'], check=True)
#
#                 # Java kodini ishga tushirish
#                 result = subprocess.run(
#                     ['java', 'User'],
#                     input = input_data,
#                     text=True,
#                     capture_output=True,
#                     timeout=5  # 5 soniya ichida kod bajarilishi kerak
#                 )
#
#             elif language == 'cpp':
#                 # C++ kodini faylga yozish
#                 with open('user_code.cpp', 'w') as code_file:
#                     code_file.write(user_code)
#
#                 # C++ kodini kompilyatsiya qilish
#                 subprocess.run(['g++', 'user_code.cpp', '-o', 'user_code.exe'], check=True)
#                 # C++ kodini ishga tushirish
#                 result = subprocess.run(
#                     ['./user_code.exe'],
#                     input=input_data,
#                     text=True,
#                     capture_output=True,
#                     timeout=10  # 5 soniya ichida kod bajarilishi kerak
#                 )
#             elif language == 'javascript':
#                 with open('user_code.js', 'w') as code_file:
#                     code_file.write(user_code)
#                 result = subprocess.run(
#                     ['node', 'user_code.js'],
#                     input=input_data,
#                     text=True,
#                     capture_output=True,
#                     timeout=5
#                 )
#
#                 # Natijani Submission obyektiga saqlash
#             submission.result = result.stdout.strip()
#             # output = result.stdout.strip()
#             # print(submission)
#             print("************************************")
#             print(submission.result)
#             # print(output)
#             # # Natijani tekshirish
#             if submission.result == expected_output:
#                 submission.result = 'Success'
#             else:
#                 submission.result = f'Failure: expected {expected_output} but got {submission.result}'
#
#         except subprocess.TimeoutExpired:
#             submission.result = 'Failure: Code execution timed out'
#
#         except subprocess.CalledProcessError as e:
#             submission.result = f'Failure: Code execution error: {e}'
#
#         except Exception as e:
#             submission.result = f'Failure: An error occurred: {e}'
#
#         submission.save()
#         return redirect('submission_result', pk=submission.pk)
#
#     return render(request, 'submissions/submit_code.html', {'problem': problem})

# submissions/views.py
# import subprocess
# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.decorators.csrf import csrf_exempt
# from problems.models import Problem
# from .models import Submission
#
#
# @csrf_exempt
# def submit_code(request, problem_id):
#     problem = get_object_or_404(Problem, pk=problem_id)
#
#     if request.method == 'POST':
#         user_code = request.POST['code']
#         language = request.POST['language']
#
#         # Yangi Submission yaratish
#         submission = Submission.objects.create(
#             user = request.user,
#             problem=problem,
#             code=user_code,
#             language=language,
#             result='',
#         )
#
#         # Test holatlarini olish
#         test_cases = problem.test_cases.strip().split('\n')
#
#         all_results = []
#         t, f = 0, 0
#         for test_case in test_cases:
#             input_data, expected_output = test_case.split(' -> ')
#             input_data = input_data.strip()
#             expected_output = expected_output.strip()
#
#             # Kodni tekshirish va natijani olish
#             try:
#                 if language == 'python':
#                     with open('user_code.py', 'w') as code_file:
#                         code_file.write(user_code)
#                     result = subprocess.run(
#                         ['python', 'user_code.py'],
#                         input=input_data,
#                         text=True,
#                         capture_output=True,
#                         timeout=5
#                     )
#
#                 elif language == 'java':
#                     with open('User.java', 'w') as code_file:
#                         code_file.write(user_code)
#                     subprocess.run(['javac', 'User.java'], check=True)
#                     result = subprocess.run(
#                         ['java', 'User'],
#                         input=input_data,
#                         text=True,
#                         capture_output=True,
#                         timeout=5
#                     )
#
#                 elif language == 'cpp':
#                     with open('user_code.cpp', 'w') as code_file:
#                         code_file.write(user_code)
#                     subprocess.run(['g++', 'user_code.cpp', '-o', 'user_code.exe'], check=True)
#                     result = subprocess.run(
#                         ['./user_code.exe'],
#                         input=input_data,
#                         text=True,
#                         capture_output=True,
#                         timeout=5
#                     )
#
#                 elif language == 'javascript':
#                     with open('user_code.js', 'w') as code_file:
#                         code_file.write(user_code)
#                     result = subprocess.run(
#                         ['node', 'user_code.js'],
#                         input=input_data,
#                         text=True,
#                         capture_output=True,
#                         timeout=5
#                     )
#
#
#                 output = result.stdout.strip()
#                 all_results.append({
#                     'input': input_data,
#                     'expected_output': expected_output,
#                     'output': output,
#                     'success': f"✅ Success\n{'-'*30}" if output == expected_output else f"❌ Error\n{'-'*30}"
#                 })
#
#
#             except subprocess.TimeoutExpired:
#                 all_results.append({
#                     'input': input_data,
#                     'expected_output': expected_output,
#                     'output': 'Timeout Error: Code execution timed out',
#                     'success': False
#                 })
#
#             except subprocess.CalledProcessError as e:
#                 all_results.append({
#                     'input': input_data,
#                     'expected_output': expected_output,
#                     'output': f'Execution Error: {e}',
#                     'success': False
#                 })
#
#             except Exception as e:
#                 all_results.append({
#                     'input': input_data,
#                     'expected_output': expected_output,
#                     'output': f'An error occurred: {e}',
#                     'success': False
#                 })
#
#         submission.result = '\n'.join([
#                                           f"Input: {res['input']}\nExpected: {res['expected_output']}\nOutput: {res['output']}\nSuccess: {res['success']}"
#                                           for res in all_results])
#         submission.save()
#         return redirect('submission_result', pk=submission.pk)
#
#     return render(request, 'submissions/submit_code.html', {'problem': problem})


# 03.06.2024 kungi chatgpt javobiga asosan
# https://chatgpt.com/share/2ac2bf27-c1f0-4bf3-80a0-0bb7ee2399ba
# submissions/views.py
import subprocess
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from problems.models import Problem
from .models import Submission


@csrf_exempt
def submit_code(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)

    if request.method == 'POST':
        user_code = request.POST['code']
        language = request.POST['language']

        # Yangi Submission yaratish
        submission = Submission.objects.create(
            user = request.user,
            problem=problem,
            code=user_code,
            language=language,
            result='',
        )

        # Test holatlarini olish
        test_cases = problem.test_cases.strip().split('\n')

        all_results = []
        success_count = 0
        error_count = 0

        for test_case in test_cases:
            input_data, expected_output = test_case.split(' -> ')
            input_data = input_data.strip()
            expected_output = expected_output.strip()

            # Kodni tekshirish va natijani olish
            try:
                if language == 'python':
                    with open('user_code.py', 'w') as code_file:
                        code_file.write(user_code)
                    result = subprocess.run(
                        ['python', 'user_code.py'],
                        input=input_data,
                        text=True,
                        capture_output=True,
                        timeout=5
                    )

                elif language == 'java':
                    with open('User.java', 'w') as code_file:
                        code_file.write(user_code)
                    subprocess.run(['javac', 'User.java'], check=True)
                    result = subprocess.run(
                        ['java', 'User'],
                        input=input_data,
                        text=True,
                        capture_output=True,
                        timeout=5
                    )

                elif language == 'cpp':
                    with open('user_code.cpp', 'w') as code_file:
                        code_file.write(user_code)
                    subprocess.run(['g++', 'user_code.cpp', '-o', 'user_code.exe'], check=True)
                    result = subprocess.run(
                        ['./user_code.exe'],
                        input=input_data,
                        text=True,
                        capture_output=True,
                        timeout=5
                    )

                elif language == 'javascript':
                    with open('user_code.js', 'w') as code_file:
                        code_file.write(user_code)
                    result = subprocess.run(
                        ['node', 'user_code.js'],
                        input=input_data,
                        text=True,
                        capture_output=True,
                        timeout=5
                    )

                output = result.stdout.strip()
                success = output == expected_output
                if success:
                    success_count += 1
                    all_results.append({
                        'input': input_data,
                        'expected_output': expected_output,
                        'output': output,
                        'success': f"✅ Success\n{'-' * 30}"
                    })
                else:
                    error_count += 1
                    all_results.append({
                        'input': input_data,
                        'expected_output': expected_output,
                        'output': output,
                        'success': f"❌ Error\n{'-' * 30}"
                    })

            except subprocess.TimeoutExpired:
                error_count += 1
                all_results.append({
                    'input': input_data,
                    'expected_output': expected_output,
                    'output': 'Timeout Error: Code execution timed out',
                    'success': f"❌ Error\n{'-' * 30}"
                })

            except subprocess.CalledProcessError as e:
                error_count += 1
                all_results.append({
                    'input': input_data,
                    'expected_output': expected_output,
                    'output': f'Execution Error: {e}',
                    'success': f"❌ Error\n{'-' * 30}"
                })

            except Exception as e:
                error_count += 1
                all_results.append({
                    'input': input_data,
                    'expected_output': expected_output,
                    'output': f'An error occurred: {e}',
                    'success': f"❌ Error\n{'-' * 30}"
                })

        submission.result = '\n'.join([
            f"Input: {res['input']}\nExpected: {res['expected_output']}\nOutput: {res['output']}\nSuccess: {res['success']}"
            for res in all_results
        ]) + f"\nTotal Success: {success_count}\nTotal Errors: {error_count}"
        submission.save()
        return render(request, 'submissions/submission_result.html', context={
            'submission': submission,
            'success': success_count,
            'error': error_count,
        })
        # return redirect('submission_result', pk=submission.pk, kwargs={'success':success_count, 'error':error_count})

    return render(request, 'submissions/submit_code.html', {'problem': problem})


def submission_result(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    return render(request, 'submissions/submission_result.html', {'submission': submission})



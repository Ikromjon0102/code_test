from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, UserUpdateForm
from django.contrib.auth import login



# class RegisterView(View):
#     def get(self, request):
#         create_user = UserCreateForm()
#
#         context = {
#             'form':create_user
#         }
#         return render(request=request, template_name='users/register.html', context=context)
#
#     def post(self, request):
#         create_form = UserCreateForm(data=request.POST)
#
#         if create_form.is_valid():
#             create_form.save()
#             return redirect('problems:problem_list')
#         else:
#             context = {
#                 'form': create_form
#             }
#             return render(request=request, template_name='users/register.html', context=context)




class RegisterView(View):
    def get(self, request):
        create_user = UserCreateForm()
        context = {
            'form': create_user
        }
        return render(request=request, template_name='users/register.html', context=context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            user = create_form.save()
            # login(request, user)
            return redirect('users:verify_email')
        else:
            context = {
                'form': create_form
            }
            return render(request=request, template_name='users/register.html', context=context)


# class LoginView(View):
#     def get(self, request):
#         login_user = UserLoginForm()
#         context = {
#             'form': login_user
#         }
#         return render(request=request, template_name='users/login.html', context = context)
#
#     def post(self, request):
#         # login_form = UserLoginForm(data=request.POST)
#
#         login_form = AuthenticationForm(data=request.POST)
#
#         if login_form.is_valid():
#             # log in the user
#             print('salom dunyo')
#             return redirect('users:register')
#         else:
#             print('nima gap ozi')
#             return render(request, 'users/login.html',{'login_form': login_form})
#
#




class LoginView(View):
    def get(self, request):
        # login_form = UserLoginForm()
        login_form = AuthenticationForm()

        return render(request=request, template_name='users/login.html',context= {'form' : login_form})

    def post(self, request):
        # print(request.POST['username'], request.POST['password'])

        # login_form = UserLoginForm(data=request.POST)

        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in')

            return redirect('problems:problem_list')
        else:
            return render(request=request, template_name='users/login.html',context= {'form' : login_form})

# class ProfileView(View):
#     def get(self, request):
#         user = request.user
#         if not user.is_authenticated:
#             return redirect('users:login')
#
#         return render(request, 'users/profile.html', {'user': request.user})


class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'users/profile.html', {'user': request.user})



class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('landing_page')


class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)

        return render(request, 'users/profile_edit.html', {'form': form})

    def post(self, request):
        form = UserUpdateForm(
            instance = request.user,
            data = request.POST,
            files = request.FILES
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'You have been updated successfully.')
            return redirect('users:profile')

        return render(request, 'users/profile_edit.html', {'form': form})


User = get_user_model()

def verify_email(request):
    if request.method == 'POST':
        code = request.POST.get('verification_code')
        try:
            user = User.objects.get(verification_code=code)
            user.email_verified = True
            user.verification_code = None  # Clear the verification code
            user.save()
            login(request, user)
            messages.success(request, 'Your email has been verified!')
            return redirect('problems:problem_list')
        except User.DoesNotExist:
            messages.error(request, 'Invalid verification code.')
    return render(request, 'users/verify_email.html')
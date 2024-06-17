from django import forms
from django.contrib.auth import login

from users.models import CustomUser


# class UserCreateForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=150)
#     last_name = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128)
#
#     def save(self):
#         username = self.cleaned_data['username']
#         firstname = self.cleaned_data['first_name']
#         lastname = self.cleaned_data['last_name']
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#
#         user = CustomUser.objects.create(
#             username=username,
#             first_name=firstname,
#             last_name=lastname,
#             email=email,
#             is_staff=True,
#             is_superuser=True
#         )
#         user.set_password(password)
#
#         user.save()

# class UserCreateForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username','email','first_name','last_name', 'gender', 'password')
#
#     def save(self, commit=True):
#         user = super().save(commit)
#
#         gender = self.cleaned_data['gender']
#         if gender == 'male':
#             user.profile_picture = 'profile_pictures/default_boy_pic.jpg'
#         elif gender == 'female':
#             user.profile_picture = 'profile_pictures/default_girl_pic.jpg'
#
#         user.set_password(self.cleaned_data['password'])
#         user.save()
#         return user

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# class UserCreateForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'first_name', 'last_name', 'gender')
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if CustomUser.objects.filter(email=email).exists():
#             raise forms.ValidationError("This email address is already in use.")
#         return email
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#
#         gender = self.cleaned_data.get('gender')
#         if gender:
#             if gender == 'male':
#                 user.profile_picture = 'profile_pictures/default_boy_pic.jpg'
#             elif gender == 'female':
#                 user.profile_picture = 'profile_pictures/default_girl_pic.jpg'
#         if commit:
#             user.save()
#         return user


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from .models import CustomUser
import random


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'gender')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        gender = self.cleaned_data.get('gender')
        if gender:
            if gender == 'male':
                user.profile_picture = 'profile_pictures/default_boy_pic.jpg'
            elif gender == 'female':
                user.profile_picture = 'profile_pictures/default_girl_pic.jpg'

        user.verification_code = generate_verification_code()

        if commit:
            user.save()
            self.send_verification_email(user)
        return user

    def send_verification_email(self, user):
        subject = "Email Verification"
        message = f"Your verification code is {user.verification_code}"
        from_email = "your_email@example.com"
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)


def generate_verification_code():
    return str(random.randint(100000, 999999))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')




# class UserLoginForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128)
#
#     # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
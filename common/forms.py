
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'nickname', 'username', 'phonenumber', 'address')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'nickname', 'username', 'phonenumber', 'address', 
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]



# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.db import models


# from django import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField

# from .models import User


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email', 'date_of_birth')

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ('email', 'password', 'date_of_birth',
#                   'is_active', 'is_admin')

#     def clean_password(self):
#         return self.initial["password"]


# class UserForm(models.Model):
#     # email = forms.EmailField(label="이메일")
    
#     # class Meta:
#         # model = User
#         # fields = ("username", "email")
#     fields = ['userid', 'password', 'nickname', 'username', 'phonenumber', 'address']
#     widgets = {
#         'userid': forms.TextInput(attrs={'placeholder': '아이디를 입력하세요.'}),
#         'password': forms.TextInput(attrs={'placeholder': '비밀번호를 입력하세요.'}),
#         'nickname': forms.TextInput(attrs={'placeholder': '별명을 입력하세요.'}),
#         'username': forms.TextInput(attrs={'placeholder': '본인의 이름을 입력하세요.'}),
#         'phonenumber': forms.TextInput(attrs={'placeholder': '전화번호를 입력하세요.'}),
#         'address': forms.TextInput(attrs={'placeholder': '주소를 입력하세요.'}),
#     }






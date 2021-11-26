from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'real_name')

    def clean_password2(self):#비밀번호가 기준이나 확인과 다를 경우를 체크
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 맞지 않습니다")
        return password2

    def save(self, commit=True):#데이터 저장
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):#사용자 정보 수정
    class Meta:
        model = User
        fields = ('email', 'password', 'real_name',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class SignupForm(UserCreationForm):#회원가입
    class Meta(UserCreationForm):
        model = User
        fields = ("email",'real_name', "password1", "password2")


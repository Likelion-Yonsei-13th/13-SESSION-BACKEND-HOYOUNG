from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        max_length=150,
        error_messages={
            "required": "아이디를 입력해주세요.",
            "unique": "이미 존재하는 아이디입니다.",
            "invalid": "유효하지 않은 아이디 형식입니다."
        }
    )
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput,
        error_messages={
            "required": "비밀번호를 입력해주세요.",
            "min_length": "비밀번호가 너무 짧습니다. 최소 8자 이상 입력해주세요.",
            "invalid": "비밀번호에 허용되지 않은 문자가 포함되어 있습니다.",
        }
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
        error_messages={
            "required": "비밀번호 확인을 입력해주세요.",
            "password_mismatch": "비밀번호가 일치하지 않습니다."
        }
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

from django import forms
from django.contrib import messages

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Kullancı Adı")
    password = forms.CharField(min_length=8,max_length=16,label="Şifre",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label="Kullanıcı Adı")
    password = forms.CharField(min_length=8, max_length=16, label="Şifre", widget=forms.PasswordInput)
    confirm = forms.CharField(min_length=8, max_length=16, label="Şifre Doğrula", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifreler Eşleşmiyor!")

        
        
        values = {
            "username":username,
            "password":password
        }
        
        return values
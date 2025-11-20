from django import forms
from .models import User

class EmailLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"input"}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

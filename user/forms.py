from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": ("input input-bordered w-full max-w-xs"),
                    "placeholder": ("Type here"),
                }
            )
        
class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": ("input input-bordered w-full max-w-xs"),
                    "placeholder": ("Type here"),
                }
            )
        
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": ("input input-bordered w-full max-w-xs"),
                    "placeholder": ("Type here"),
                }
            )
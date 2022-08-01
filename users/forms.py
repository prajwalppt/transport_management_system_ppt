from django import forms
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))


# class SignUpForm(UserCreationForm):
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password(Again)')
#     # first_name = models.CharField(_('first name'), max_length=150, blank=True)
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name']
        # widgets = {'username':forms.TextInput(attrs={'class':'form-control','readonly':True}),
        # 'first_name':forms.TextInput(attrs={'class':'form-control'}),
        # 'last_name':forms.TextInput(attrs={'class':'form-control'}),
        # }

        # error_messages = {
        #     'first_name':{'required':'This field is required.'},
        #     'last_name':{'required':'This field is required.'}
        # }
        # # labels = {'username':'Email'}
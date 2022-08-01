from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View

from .forms import LoginForm

# Create your views here.
def login_page(request):
    print("login called")
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        print(forms)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)

            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


# class SignUp(View):
#     def get(self,request):
#         print()
#         form = SignUpForm()
#         return render(request,'users/signup.html',{'form':form})
#     def post(self,request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # email = form.cleaned_data['username']
#             # user = User.objects.get(username=email)
#             # user.email = email
#             # user.save()
#             # messages.success(request,f'Account Created Successfully {email}')
#             return HttpResponseRedirect('/signup/')
#         else:
#             return render(request,'users/signup.html',{'form':form})


def logout_page(request):
    print("log out")
    logout(request)
    return redirect('login')

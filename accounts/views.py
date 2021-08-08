
from accounts.forms import LoginForm
from django.shortcuts import redirect, render, reverse
from django.views import View
from django.contrib.auth import authenticate, get_user_model, login, logout
from accounts.forms import LoginForm, RegisterForm




class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('posts_list_url'))

        login_form = LoginForm()

        return render(request, 'accounts/login.html', context={'login_form': login_form})

    
    def post(self, request):
        bound_form = LoginForm(request.POST)
        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                    login(request, user)
                    return redirect(reverse('posts_list_url'))
            return render(request, 'accounts/login.html', context={'bound_form': bound_form})



class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('posts_list_url'))

        register_form = RegisterForm()

        return render(request, 'accounts/register.html', context={'register_form': register_form})

    
    def post(self, request):
        bound_form = RegisterForm(request.POST)
        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            User = get_user_model()
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
            return redirect(reverse('posts_list_url'))
        return render(request, 'accounts/register.html', context={'bound_form': bound_form})
                    
def logout_view(request):
    logout(request)      
    return redirect(reverse('login_url'))  

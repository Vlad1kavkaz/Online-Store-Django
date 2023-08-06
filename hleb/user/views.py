from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm, EditUserForm

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user\\register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистрация'
        context['cat_selected'] = 0

        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class loginUser(LoginView):
    template_name = 'user\\login.html'
    form_class = LoginUserForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистрация'
        context['cat_selected'] = 0

        return context

def account(request):
    return render(request, 'user\\account.html')

def logout_user(request):
    logout(request)
    return redirect('home_page')

def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('home_page')
        else:
            form = EditUserForm(instance=request.user)
        return render(request, 'user\\account.html', {'form': form})
    else:
        return redirect('login')
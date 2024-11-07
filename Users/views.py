from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from Users.forms import UserRegisterForm, UserProfileForm
from Users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'Users/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save(commit=False)

        # Если аватар загружен, сохраняем его
        if 'avatar' in self.request.FILES:
            user.avatar = self.request.FILES['avatar']

        user.save()

        # Авторизуем пользователя
        login(self.request, user)

        # Перенаправляем на страницу авторизации
        return redirect(self.success_url)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'Users/user_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_object(self, queryset=None):
        return self.request.user


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                remember_me = request.POST.get('remember', False)
                if remember_me:
                    # Устанавливаем длительные сессии (например, 1 месяц)
                    request.session.set_expiry(2592000)  # 30 дней
                else:
                    request.session.set_expiry(0)  # Сессия будет длиться до закрытия браузера

                login(request, user)
                return redirect('blog:blog_list')  # Перенаправление после успешного входа
    else:
        form = AuthenticationForm()

    return render(request, 'user:login.html', {'form': form})
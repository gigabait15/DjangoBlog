from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from Users.apps import UsersConfig
from Users.views import RegisterView, ProfileView


app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
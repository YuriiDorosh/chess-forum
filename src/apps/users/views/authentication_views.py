from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

from users.forms import RegistrationForm, LoginForm
from users.models import User


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy("users:profile", kwargs={"pk": user.id})


class UserRegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


def user_logout(request):
    logout(request)
    return redirect("login")

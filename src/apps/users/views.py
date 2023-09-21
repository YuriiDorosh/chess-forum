from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView


from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator


from users.forms import RegistrationForm, LoginForm, UserProfileForm
from users.models import User
from posts.models import UserPost


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


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(User, id=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_posts = UserPost.objects.filter(user=self.object)
        context['user_posts'] = user_posts
        return context

class UserProfileEditView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile_edit.html"

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        if self.request.user.is_authenticated and user_id == self.request.user.id:
            return get_object_or_404(User, id=user_id)
        raise Http404("You are not authorized to edit this profile.")


def user_logout(request):
    logout(request)
    return redirect("login")

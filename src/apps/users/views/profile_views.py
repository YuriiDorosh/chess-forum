from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.http import Http404

from users.forms import  UserProfileForm
from users.models import User
from posts.models import UserPost


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
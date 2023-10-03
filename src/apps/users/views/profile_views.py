from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.http import Http404

from users.forms.profile_forms import UserProfileForm
from users.models.user import User
from posts.models import UserPost
from discussions.models import Discussion


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        user_id = self.kwargs.get("pk")
        return get_object_or_404(User, id=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_posts = UserPost.objects.filter(user=self.object)
        liked_posts = UserPost.objects.filter(likes__in=[self.object])
        user_discussions = Discussion.objects.filter(author=self.object)
        context["user_posts"] = user_posts
        context["liked_posts"] = liked_posts
        context["user_discussions"] = user_discussions
        return context


class UserProfileEditView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile_edit.html"

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_object(self, queryset=None):
        user_id = self.kwargs.get("pk")
        if self.request.user.is_authenticated and user_id == self.request.user.id:
            return get_object_or_404(User, id=user_id)
        raise Http404("You are not authorized to edit this profile.")

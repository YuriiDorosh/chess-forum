from discussions.models import Discussion
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from posts.models import UserPost
from users.forms.profile_forms import UserProfileForm
from users.models.user import User

class UserProfileView(UpdateView):
    """
    View for displaying a user's profile.

    Attributes:
        model (User): The User model.
        form_class (UserProfileForm): The form used for editing the profile.
        template_name (str): The template used for displaying the profile.

    Methods:
        get_object(self, queryset=None): Retrieves the user object to be displayed.
        get_context_data(self, **kwargs): Adds user's posts, liked posts, and discussions to the context.

    Template:
        users/profile.html
    """
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        """
        Retrieves the user object to be displayed.

        Args:
            queryset: The queryset to filter the user object.

        Returns:
            User: The user object.
        """
        user_id = self.kwargs.get("pk")
        return get_object_or_404(User, id=user_id)

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to the view.

        Context:
            user_posts (QuerySet): User's posts.
            liked_posts (QuerySet): User's liked posts.
            user_discussions (QuerySet): User's discussions.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The updated context data.
        """
        context = super().get_context_data(**kwargs)
        user_posts = UserPost.objects.filter(user=self.object)
        liked_posts = UserPost.objects.filter(likes__in=[self.object])
        user_discussions = Discussion.objects.filter(author=self.object)
        context["user_posts"] = user_posts
        context["liked_posts"] = liked_posts
        context["user_discussions"] = user_discussions
        return context

class UserProfileEditView(UpdateView):
    """
    View for editing a user's profile.

    Attributes:
        model (User): The User model.
        form_class (UserProfileForm): The form used for editing the profile.
        template_name (str): The template used for editing the profile.

    Methods:
        get_success_url(self): Determines the URL to redirect after successful profile editing.
        get_object(self, queryset=None): Retrieves the user object to be edited.

    Template:
        users/profile_edit.html
    """
    model = User
    form_class = UserProfileForm
    template_name = "users/profile_edit.html"

    def get_success_url(self):
        """
        Determines the URL to redirect after successful profile editing.

        Returns:
            str: The URL to redirect to.
        """
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_object(self, queryset=None):
        """
        Retrieves the user object to be edited.

        Checks if the user is authenticated and if the provided user ID matches the current user's ID.

        Args:
            queryset: The queryset to filter the user object.

        Returns:
            User: The user object.

        Raises:
            Http404: If the user is not authorized to edit this profile.
        """
        user_id = self.kwargs.get("pk")
        if self.request.user.is_authenticated and user_id == self.request.user.id:
            return get_object_or_404(User, id=user_id)
        raise Http404("You are not authorized to edit this profile.")

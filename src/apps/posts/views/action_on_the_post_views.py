from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404, get_object_or_404, redirect, render
from django.views import View
from posts.forms.post_forms import UserPostCreateForm, UserPostUpdateForm
from posts.models.post import UserPost
from posts.services.user_post_service import UserPostService


class CreateUserPostView(View):
    """
    View for creating a new user post.

    Attributes:
        template_name (str): The path to the HTML template for displaying the post creation form.

    Methods:
        get(self, request): Displays the form for creating a new post.
        post(self, request): Handles the submitted form for creating a new post.

    Template:
        posts/create_post.html
    """

    template_name = "posts/create_post.html"

    def get(self, request):
        """
        Displays the form for creating a new user post.

        Args:
            request: The HTTP request.

        Returns:
            HttpResponse: Response with the post creation form.
        """
        form = UserPostCreateForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        """
        Handles the submitted form for creating a new user post.

        Args:
            request: The HTTP request.

        Returns:
            HttpResponseRedirect: Redirects the user to the page with a list of posts
            after successfully creating a new post.
        """
        form = UserPostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            image = form.cleaned_data['image'] if 'image' in form.cleaned_data else None

            UserPostService.create_user_post(request.user, form_data, image)
            return redirect("posts:all_user_posts")

        return render(request, self.template_name, {"form": form})


class EditUserPostView(View):
    """
    View for editing a user post.

    Attributes:
        template_name (str): The path to the HTML template for displaying the post editing form.

    Methods:
        get(self, request, post_id): Displays the form for editing a user post.
        post(self, request, post_id): Handles the submitted form for editing a user post.

    Template:
        posts/edit_post.html
    """

    template_name = "posts/edit_post.html"

    @staticmethod
    def get_user(request):
        if request.user.is_authenticated:
            return request.user
        return None

    @login_required
    def get(self, request, post_id):
        """
        Displays the form for editing a user post.

        Args:
            request: The HTTP request.
            post_id (int): The ID of the post to be edited.

        Returns:
            HttpResponse: Response with the post editing form.
        """
        post = get_object_or_404(UserPost, id=post_id)
        user = self.get_user(request)

        if post.user != request.user:
            raise Http404("Post not found or you don't have permission to edit it")

        form = UserPostUpdateForm(instance=post)
        return render(request, self.template_name, {"form": form, "post": post})

    @login_required
    def post(self, request, post_id):
        """
        Handles the submitted form for editing a user post.

        Args:
            request: The HTTP request.
            post_id (int): The ID of the post to be edited.

        Returns:
            HttpResponseRedirect: Redirects the user to the page with a list of posts
            after successfully editing a user post.
        """
        post = get_object_or_404(UserPost, id=post_id)
        user = self.get_user(request)

        if post.user != request.user:
            raise Http404("Post not found or you don't have permission to edit it")

        form = UserPostUpdateForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            UserPostService.edit_user_post(post_id, request.user, form.cleaned_data)
            return redirect("posts:all_user_posts")

from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404, get_object_or_404, redirect, render
from django.views import View
from posts.forms import UserPostCreateForm, UserPostUpdateForm
from posts.models.post import UserPost

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

    @login_required
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

    @login_required
    def post(self, request):
        """
        Handles the submitted form for creating a new user post.

        Args:
            request: The HTTP request.

        Returns:
            HttpResponseRedirect: Redirects the user to the page with a list of posts
            after successfully creating a new post.
        """
        form = UserPostCreateForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect("posts:all_user_posts")

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

        if post.user != request.user:
            raise Http404("Post not found or you don't have permission to edit it")

        form = UserPostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:all_user_posts")

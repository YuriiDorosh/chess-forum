from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404, get_object_or_404, redirect, render
from django.views import View
from posts.forms import UserPostCreateForm, UserPostUpdateForm
from posts.models.post import UserPost


class CreateUserPostView(View):
    template_name = "posts/create_post.html"

    def get(self, request):
        form = UserPostCreateForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserPostCreateForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect("posts:all_user_posts")


class EditUserPostView(View):
    template_name = "posts/edit_post.html"

    def get(self, request, post_id):
        post = get_object_or_404(UserPost, id=post_id)

        if post.user != request.user:
            raise Http404("Post not found or you don't have permission to edit it")

        form = UserPostUpdateForm(instance=post)
        return render(request, self.template_name, {"form": form, "post": post})

    def post(self, request, post_id):
        post = get_object_or_404(UserPost, id=post_id)

        if post.user != request.user:
            raise Http404("Post not found or you don't have permission to edit it")

        form = UserPostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:all_user_posts")

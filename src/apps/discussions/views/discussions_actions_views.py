from discussions.forms.discussion_forms import DiscussionForm
from discussions.services.discussion_service import DiscussionService
from django.shortcuts import redirect, render
from django.views import View


class CreateDiscussionView(View):
    """
    View for creating discussions.

    GET request:
    Renders a form to create a discussion.

    POST request:
    Processes the form data, creates a discussion, and redirects to the discussion list if the form is valid.
    """

    def get(self, request):
        form = DiscussionForm()
        return render(request, "discussions/create_discussion.html", {"form": form})

    def post(self, request):
        """
        Handles the POST request for creating discussions.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirects to the discussion list on success or re-renders the form on failure.
        """
        if request.method == "POST":
            form = DiscussionForm(request.POST, request.FILES)
            if form.is_valid():
                DiscussionService.create_discussion(request.user, form.cleaned_data)
                return redirect("discussions:discussion_list")
        else:
            form = DiscussionForm()
        return render(request, "discussions/create_discussion.html", {"form": form})


class ClosedDiscussionsView(View):
    """
    View for displaying closed discussions.

    GET request:
    Retrieves and renders a list of closed discussions.
    """

    def get(self, request):
        closed_discussions = DiscussionService.get_closed_discussions()
        return render(request, "discussions/closed_discussions.html", {"closed_discussions": closed_discussions})

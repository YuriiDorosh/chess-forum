from django.shortcuts import redirect, render
from django.views import View

from discussions.forms.discussion_forms import DiscussionForm
from discussions.services.discussion_service import DiscussionService


class CreateDiscussionView(View):
    def get(self, request):
        form = DiscussionForm()
        return render(request, "discussions/create_discussion.html", {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = DiscussionForm(request.POST, request.FILES)
            if form.is_valid():
                DiscussionService.create_discussion(request.user, form.cleaned_data)
                return redirect("discussions:discussion_list")
        else:
            form = DiscussionForm()
        return render(request, "discussions/create_discussion.html", {"form": form})

class ClosedDiscussionsView(View):
    def get(self, request):
        closed_discussions = DiscussionService.get_closed_discussions()
        return render(request, "discussions/closed_discussions.html", {"closed_discussions": closed_discussions})

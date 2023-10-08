from discussions.forms.reply_forms import ReplyForm
from discussions.forms.reply_like_forms import ReplyLikeForm
from discussions.services.discussion_service import DiscussionService
from discussions.services.reply_like_service import ReplyLikeService
from discussions.services.reply_service import ReplyService
from django.shortcuts import redirect, render
from django.views import View


class DiscussionListView(View):
    """
    View for displaying a list of discussions.

    GET request:
    Retrieves and renders a list of discussions.
    """

    def get(self, request):
        discussions = DiscussionService.get_all_discussions()
        return render(
            request, "discussions/discussion_list.html", {"discussions": discussions}
        )


class DiscussionDetailView(View):
    """
    View for displaying details of a discussion.

    GET request:
    Retrieves and renders the details of a specific discussion and its replies.

    POST request:
    Processes the form data to create a reply, toggle a reply like, or close the discussion (if authorized).
    """

    def get(self, request, discussion_id):
        discussion = DiscussionService.get_discussion_by_id(discussion_id)
        replies = ReplyService.get_replies_for_discussion(discussion)
        initial_data = {"discussion_id": discussion_id}
        reply_form = ReplyForm(initial=initial_data)
        return render(
            request,
            "discussions/discussion_detail.html",
            {"discussion": discussion, "replies": replies, "reply_form": reply_form},
        )

    def post(self, request, discussion_id):
        discussion = DiscussionService.get_discussion_by_id(discussion_id)
        replies = ReplyService.get_replies_for_discussion(discussion)

        if request.method == "POST":
            if "close_discussion" in request.POST and request.user == discussion.author:
                DiscussionService.close_discussion(discussion)
                return redirect("discussions:discussion_list")

            reply_form = ReplyForm(request.POST, request.FILES)
            if reply_form.is_valid():
                ReplyService.create_reply(
                    discussion, request.user, reply_form.cleaned_data
                )
                return redirect(
                    "discussions:discussion_detail", discussion_id=discussion_id
                )

            like_form = ReplyLikeForm(request.POST)
            if like_form.is_valid():
                reply_id = like_form.cleaned_data["reply_id"]
                reply_to_like = ReplyService.get_reply_by_id(reply_id)
                ReplyLikeService.toggle_like(request.user, reply_to_like)

        else:
            reply_form = ReplyForm()
            like_form = ReplyLikeForm()

        return render(
            request,
            "discussions/discussion_detail.html",
            {
                "discussion": discussion,
                "replies": replies,
                "reply_form": reply_form,
                "like_form": like_form,
            },
        )

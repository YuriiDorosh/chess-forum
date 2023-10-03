from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import Http404

from discussions.models import Discussion, Reply, ReplyLike
from discussions.forms import DiscussionForm, ReplyForm


def discussion_list(request):
    discussions = Discussion.objects.all()
    return render(request, "discussions/discussion_list.html", {"discussions": discussions})


def discussion_detail(request, discussion_id):
    discussion = Discussion.objects.get(pk=discussion_id)
    replies = Reply.objects.filter(discussion=discussion).annotate(like_count=Count("likes")).order_by("-date_added")
    reply_form = ReplyForm()

    if request.method == "POST":
        # if discussion.closed:
        #     raise Http404("This discussion is closed.")
        reply_form = ReplyForm(request.POST, request.FILES)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.discussion = discussion
            reply.author = request.user
            reply.save()
            return redirect("discussion_detail", discussion_id=discussion_id)

        if "like_reply" in request.POST:
            reply_id = request.POST["like_reply"]
            reply_to_like = Reply.objects.get(pk=reply_id)
            like, created = ReplyLike.objects.get_or_create(reply=reply_to_like, user=request.user)
            if not created:
                like.delete()

        if "close_discussion" in request.POST and request.user == discussion.author:
            discussion.closed = True
            discussion.save()

    return render(
        request,
        "discussions/discussion_detail.html",
        {"discussion": discussion, "replies": replies, "reply_form": reply_form},
    )


def create_discussion(request):
    if request.method == "POST":
        form = DiscussionForm(request.POST, request.FILES)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.author = request.user
            discussion.save()
            return redirect("discussions:discussion_list")
    else:
        form = DiscussionForm()
    return render(request, "discussions/create_discussion.html", {"form": form})


def closed_discussions(request):
    closed_discussions = Discussion.objects.filter(closed=True)
    return render(request, "discussions/closed_discussions.html", {"closed_discussions": closed_discussions})

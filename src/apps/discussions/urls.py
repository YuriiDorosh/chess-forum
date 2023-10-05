from discussions.views.discussions_actions_views import (
    ClosedDiscussionsView,
    CreateDiscussionView,
)
from discussions.views.discussions_detail_views import (
    DiscussionDetailView,
    DiscussionListView,
)
from django.urls import path

app_name = "discussions"

urlpatterns = [
    path("", DiscussionListView.as_view(), name="discussion_list"),
    path(
        "<uuid:discussion_id>/",
        DiscussionDetailView.as_view(),
        name="discussion_detail",
    ),
    path("create/", CreateDiscussionView.as_view(), name="create_discussion"),
    path("closed/", ClosedDiscussionsView.as_view(), name="closed_discussions"),
]

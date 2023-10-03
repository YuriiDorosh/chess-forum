from django.urls import path
from discussions import views

app_name = "discussions"

urlpatterns = [
    path("", views.discussion_list, name="discussion_list"),
    # path('discussion/<uuid:discussion_id>/', views.discussion_detail, name='discussion_detail'),
    path("<uuid:discussion_id>/", views.discussion_detail, name="discussion_detail"),
    path("create/", views.create_discussion, name="create_discussion"),
    path("closed/", views.closed_discussions, name="closed_discussions"),
]

from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import authentication_views, profile_views

app_name = "users"

urlpatterns = [
    path("registration/", authentication_views.UserRegistrationView.as_view(), name="registration"),
    path("login/", authentication_views.UserLoginView.as_view(), name="login"),
    path("profile/<uuid:pk>", login_required(profile_views.UserProfileView.as_view()), name="profile"),
    path("profile/edit/<uuid:pk>/", login_required(profile_views.UserProfileEditView.as_view()), name="profile_edit"),
    path("logout/", authentication_views.user_logout, name="logout"),
]

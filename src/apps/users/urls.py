from django.contrib.auth.decorators import login_required
from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("registration/", views.UserRegistrationView.as_view(), name="registration"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("profile/<int:pk>", login_required(views.UserProfileView.as_view()), name="profile"),
    path("logout/", views.user_logout, name="logout"),
]

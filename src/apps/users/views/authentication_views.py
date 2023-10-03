from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms.authentication_forms import LoginForm, RegistrationForm
from users.models.user import User


class UserLoginView(LoginView):
    """
    View for user login.

    Attributes:
        template_name (str): The template used for displaying the login form.
        form_class (LoginForm): The form used for user login.

    Methods:
        get_success_url(self): Determines the URL to redirect after successful login.

    Template:
        users/login.html
    """

    template_name = "users/login.html"
    form_class = LoginForm

    def get_success_url(self):
        """
        Determines the URL to redirect after successful login.

        Returns:
            str: The URL to redirect to.
        """
        user = self.request.user
        return reverse_lazy("users:profile", kwargs={"pk": user.id})


class UserRegistrationView(CreateView):
    """
    View for user registration.

    Attributes:
        model (User): The User model.
        form_class (RegistrationForm): The form used for user registration.
        template_name (str): The template used for displaying the registration form.
        success_url (str): The URL to redirect after successful registration.

    Template:
        users/register.html
    """

    model = User
    form_class = RegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


def user_logout(request):
    """
    View for user logout.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the login page after logout.
    """
    logout(request)
    return redirect("login")

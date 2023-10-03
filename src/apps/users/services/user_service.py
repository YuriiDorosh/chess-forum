from django.shortcuts import get_object_or_404
from users.models.user import User

class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        """
        Retrieves a user by their ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            User: The user object if found, or raises a 404 exception if not found.
        """
        return get_object_or_404(User, id=user_id)

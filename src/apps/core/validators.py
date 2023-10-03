from django.core.exceptions import ValidationError


def validate_chess_profile_url(value):
    if not value.startswith("https://www.chess.com/member/"):
        raise ValidationError("Invalid chess profile URL. It should start with 'https://www.chess.com/member/'.")


def validate_chess_game_url(value):
    if not value.startswith("https://www.chess.com/game/"):
        raise ValidationError("Invalid chess profile URL. It should start with 'https://www.chess.com/game/'.")

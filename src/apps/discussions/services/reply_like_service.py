from discussions.models.reply_like import ReplyLike

class ReplyLikeService:
    @staticmethod
    def toggle_like(user, reply):
        like, created = ReplyLike.objects.get_or_create(user=user, reply=reply)

        if not created:
            like.delete()

        return created
from discussions.models.reply import Reply


class ReplyService:
    @staticmethod
    def get_replies_for_discussion(discussion):
        return Reply.objects.filter(discussion=discussion)

    @staticmethod
    def create_reply(discussion, author, data):
        reply = Reply(discussion=discussion, author=author, **data)
        reply.save()
        return reply

    @staticmethod
    def get_reply_by_id(reply_id):
        return Reply.objects.get(pk=reply_id)

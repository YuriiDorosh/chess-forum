from discussions.models.discussion import Discussion


class DiscussionService:
    @staticmethod
    def get_all_discussions():
        return Discussion.objects.all()

    @staticmethod
    def get_discussion_by_id(discussion_id):
        return Discussion.objects.get(pk=discussion_id)

    @staticmethod
    def create_discussion(author, data):
        discussion = Discussion(author=author, **data)
        discussion.save()
        return discussion

    @staticmethod
    def close_discussion(discussion):
        discussion.closed = True
        discussion.save()

    @staticmethod
    def get_closed_discussions():
        return Discussion.objects.filter(closed=True)

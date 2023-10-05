from datetime import timedelta

from celery import shared_task
from django.utils import timezone
from room_messages.models.message import Message


@shared_task
def delete_old_messages():
    one_month_ago = timezone.now() - timedelta(days=30)

    Message.objects.filter(date_added__lt=one_month_ago).delete()

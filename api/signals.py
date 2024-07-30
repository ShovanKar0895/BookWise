import time
from django.db.models.signals import pre_save
from django.dispatch import receiver
from api.models import BookModel

@receiver(pre_save, sender=BookModel)
def set_added_date(sender, instance, **kwargs):
    if instance.pk is None:
        instance.added_date = int(time.time())
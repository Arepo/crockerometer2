from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Vote, Rating

@receiver(pre_save, sender=Vote)
def print_save_and_change_rating(sender, **kwargs)
  rating = Rating.objects.get(kwargs['instance'].id)
  rating.average_score = 8
  rating.save()

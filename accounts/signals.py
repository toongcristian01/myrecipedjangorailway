from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from .models import Profile

# #register signals
from django.dispatch import receiver

# #User send some info about the user being created
@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs): #sender=Model, instance=particular user, created=boolean 
  print('sender', sender)
  print('instance', instance)


  #if user is created, new instance created
  if created:
    Profile.objects.create(
      user=instance
      )
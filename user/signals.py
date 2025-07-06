from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
import os
from django.conf import settings

@receiver(post_save,sender=User)
def profile_creator(sender,instance,created,**kwargs):
    print("profile triggered")
    if created:
        print("created")
        profile=Profile.objects.create(user=instance)
        profile.save()
        
@receiver(pre_save, sender=Profile)
def media_cleaner(sender, instance, **kwargs):
    default_image = 'profile-pics/default.jpg'
    
    if not instance.pk:
        # New profile being created — nothing to delete
        return

    try:
        old_instance = Profile.objects.get(pk=instance.pk)
    except Profile.DoesNotExist:
        return

    old_image = old_instance.image
    new_image = instance.image

    if old_image != new_image and old_image.name != default_image:
        old_image_path = os.path.join(settings.MEDIA_ROOT, old_image.name)
        if os.path.exists(old_image_path):
            os.remove(old_image_path)
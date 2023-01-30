from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('HASD;FLKJSDF;LKJDS;FLKSDA;LFJAS;DLKJA;DSLKJADS;LKJ\n\n\n\n\n\n111111111111111111111111111111111')

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print('HASD;FLKJSDF;LKJDS;FLKSDA;LFJAS;DLKJA;DSLKJADS;LKJ\n\n\n\n\n\n222222222222222222222222222222222')
    try:
        instance.profile.save()


    except Exception as e:
        print("should see this if the user didn't have a profile originally\n" + str(e))
        instance.profile = Profile(user=instance)
        instance.profile.save()
        # print("error")

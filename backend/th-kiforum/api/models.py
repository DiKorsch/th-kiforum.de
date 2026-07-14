import random

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from mdeditor.fields import MDTextField

# Create your models here.

class Organisation(models.Model):
    name = models.CharField(max_length=255)

    description = models.TextField()

    website = models.URLField()

    def __str__(self):
        return self.name

class ContactPerson(models.Model):
    name = models.CharField(max_length=255)

    email = models.EmailField()

    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Demonstrator(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    key = models.CharField(max_length=255, unique=True)

    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)

@receiver(post_save, sender=Demonstrator)
def generate_key(sender, instance, created: bool, raw: bool, **kwargs):
    # generates a unique four character key for the Demonstrator object after it is created.
    if not created or raw:
        return
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    while True:
        key = ''.join(random.choice(CHARS) for _ in range(4))
        if not Demonstrator.objects.filter(key=key).exists():
            break

    instance.key = key
    instance.save()


class Content(models.Model):
    name = models.CharField(max_length=255, unique=True)

    content = MDTextField() #models.TextField()

    def __str__(self):
        return self.name

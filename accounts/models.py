from django.contrib.auth.models import AbstractUser

from django.db import models
from django.utils.text import slugify


class User(AbstractUser):

    def get_or_create_publisher(self):
        return Publisher.objects.get_or_create(user_ptr=self, defaults={"slug": self.username})[0]


class Publisher(User):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='publishers/logos/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    social_media = models.JSONField(blank=True, null=True)
    date_founded = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({'active' if self.is_active else 'inactive'})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

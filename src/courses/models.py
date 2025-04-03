from django.db import models
from cloudinary.models import CloudinaryField
import helpers

# Create your models here.

# call cloudinary function
helpers.cloudinary_init()


class AccessRequireMent(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email Required"


class PublishStatus(models.TextChoices):
    COMING_SOON = "upcoming", "Coming Soon"
    PUBLISHED = "publish", "Published"
    DRAFT = "draft", "Draft"


def handle_upload(instance, file_name):
    return f"{file_name}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField(blank=True, null=True, upload_to=handle_upload)
    image = CloudinaryField("image", null=True, blank=True)

    access = models.CharField(
        max_length=25, choices=AccessRequireMent, default=AccessRequireMent.EMAIL_REQUIRED)

    status = models.CharField(
        max_length=25, choices=PublishStatus, default=PublishStatus.DRAFT)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

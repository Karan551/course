from django.db import models
from cloudinary.models import CloudinaryField
import helpers
from cloudinary import CloudinaryImage
from django.utils import timezone
from django.utils.text import slugify
import uuid

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


def genertate_public_id(instance, *args, **kwargs):
    title = instance.title
    unique_id = str(uuid.uuid4()).replace("-", "")
    if not title:
        return unique_id

    short_unique_id = unique_id[:5]
    slug = slugify(title)
    return f"course/{slug}-{short_unique_id}"


def get_display_name(instance, *args, **kwargs):
    print("this is instance::", instance)

    if hasattr(instance, "get_display_name"):
        return instance.get_display_name()

    elif hasattr(instance, "title"):
        return instance.title

    model_class = instance.__class__
    model_name = model_class.__name__

    return f"{model_name} Course upload"


def get_public_id_prefix(instance, *args, **kwargs):
    if hasattr(instance, "path"):
        path = instance.path
        if path.startswith("/"):
            path = path[1:]
        if path.endswith("/"):
            path = path[:-1]

        return path

    public_id = instance.public_id

    model_class = public_id.__class__
    print("this is model name::", model_class)
    model_name = model_class.__name__
    model_name_slug = slugify(model_name)

    if not public_id:
        return f"{model_name_slug}"

    return f"{model_name_slug}/{public_id}"

    # title = instance.title

    # if title:
    #     slug = slugify(title)
    #     unique_id = str(uuid.uuid4()).replace("-", "")[:5]
    #     return f"course/{slug}-{unique_id}"

    # if instance.id:
    #     return f"course/{instance.id}"

    # return "Course Uploaded"


def handle_upload(instance, file_name):
    return f"{file_name}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    public_id = models.CharField(max_length=150, null=True, blank=True)

    # image = models.ImageField(blank=True, null=True, upload_to=handle_upload)
    image = CloudinaryField("image",
                            null=True,
                            blank=True,
                            display_name=get_display_name,
                            public_id_prefix=get_public_id_prefix,
                            tags=["course", "thumbnail"]
                            )

    access = models.CharField(
        max_length=25, choices=AccessRequireMent, default=AccessRequireMent.EMAIL_REQUIRED)

    status = models.CharField(
        max_length=25, choices=PublishStatus, default=PublishStatus.DRAFT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = genertate_public_id(self)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return self.path

    @property
    def path(self):
        return f"/courses/{self.public_id}"

    def get_display_name(self):
        return f"{self.title} - Course"

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED


    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    public_id = models.CharField(max_length=150, null=True, blank=True)
    order = models.IntegerField(default=0)
    thumbnail = CloudinaryField("image",
                                public_id_prefix=get_public_id_prefix,
                                display_name=get_display_name,
                                tags=["thumbnail", "lesson"],
                                null=True,
                                blank=True)
    video = CloudinaryField("video",
                            blank=True,
                            null=True,
                            public_id_prefix=get_public_id_prefix,
                            display_name=get_display_name,
                            tags=["video", "lesson"],
                            resource_type="video")
    can_preview = models.BooleanField(default=False,
                                      help_text="If user does not have access this course.Can they see this ?")
    status = models.CharField(
        max_length=50, choices=PublishStatus, default=PublishStatus.PUBLISHED)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = genertate_public_id(self)

        super().save(*args, **kwargs)

    @property
    def path(self):
        course_path = self.course.path

        if course_path.endswith("/"):
            course_path = course_path[:-1]

        return f"{course_path}/lesson/{self.public_id}"

    def get_display_name(self):
        return f"{self.title}-{self.course.get_display_name()}"

    class Meta:
        ordering = ["order", "-updated_at"]

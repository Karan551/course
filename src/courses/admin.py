from django.contrib import admin
from .models import Course, Lesson
from django.utils.html import format_html
from helpers import get_cloudinary_image_object, get_cloudinary_video_object

# Register your models here.

admin.site.site_header = "Course Admin Panel"
admin.site.index_title = "Course Site administration"
admin.site.site_title = "Admin Panel"


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0
    readonly_fields = [
        "updated_at",
        "public_id",
        "display_image",
        "display_video"

    ]

    def display_image(self, obj, *args, **kwargs):

        img_url = get_cloudinary_image_object(
            obj, field_name="thumbnail", width=700)

        return format_html(f"<img src={img_url} alt={obj.title}  />")

    display_image.short_description = f"Current Lesson Image"

    def display_video(self, obj, *args, **kwargs):
        video_url = get_cloudinary_video_object(
            obj, field_name="video", sign_url=False, width=600, height=600, as_html=True)

        
        return video_url

    display_video.short_description = "Video"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ["title", "status", "access"]
    list_filter = ["status", "access"]

    fields = ["public_id", "title", "description", "status",
              "image", "access", "display_image"]

    readonly_fields = ["display_image",
                       "created_at", "updated_at", "public_id"]

    def display_image(self, obj, *args, **kwargs):

        img_url = get_cloudinary_image_object(
            obj, field_name="image", width=500)

        # return format_html(img_url)
        print("this is img url in course--", img_url)
        return format_html(f"<img src={img_url} alt={obj.image}/>")

    display_image.short_description = "Current Image"

from django.contrib import admin
from .models import Course
from django.utils.html import format_html
from cloudinary import CloudinaryImage

# Register your models here.

admin.site.site_header = "Course Admin Panel"
admin.site.index_title = "Course Site administration"
admin.site.site_title = "Admin Panel"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "access"]
    list_filter = ["status", "access"]

    fields = ["title", "description", "status",
              "image", "access", "display_image"]

    readonly_fields = ["display_image"]

    def display_image(self, obj, *args, **kwargs):
        url = obj.image.url
        cloudinary_id = str(obj.image)
        cloudinary_html = obj.image.image(width=500)

        # this is another method to change image size
        cloudinary_html_2 = CloudinaryImage(cloudinary_id).image(width=500)

        return format_html(cloudinary_html_2)

    display_image.short_description = "Current Image"

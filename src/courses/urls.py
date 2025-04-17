from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("courses/course-list", views.course_list_view, name="course_list"),
    path("courses/<slug:course_id>/",
         views.course_detail_view, name="course_detail"),

    path("courses/<slug:course_id>/lessons-list/",
         views.lesson_list_view, name="lesson_list"),
    path("courses/<slug:course_id>/lesson/<slug:lesson_id>/",
         views.lesson_detail_view, name="lesson_list")
]

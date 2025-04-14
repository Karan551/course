from django.urls import path
from . import views

urlpatterns = [
    # path("", views.homepage_view, name="homepage")
    path("", views.course_list_view, name="course_list"),
    path("courses/<int:course_id>/", views.course_detail_view, name="course_detail"),
    
     path("courses/<int:course_id>/lessons-list/", views.lesson_list_view, name="lesson_list"),
      path("courses/<int:course_id>/lesson/<int:lesson_id>/", views.lesson_detail_view, name="lesson_list")
]

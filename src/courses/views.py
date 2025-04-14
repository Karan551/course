from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .services import get_publish_course, get_course_detail, get_lesson_list, get_lesson_detail
# Create your views here.


def homepage_view(request):
    return HttpResponse("<h1 style='color:blue;'>Django Course Project.</h1>")


def course_list_view(request):
    queryset = get_publish_course()
    context = {
        "courses": queryset
    }
 
    return JsonResponse({"msg": "success", "data": [x.id for x in queryset]})
    return render(request, "courses/course_list.html", context)


def course_detail_view(request, course_id):
    course_obj = get_course_detail(course_id)

    if course_obj is None:
        print("no course found")
        return Http404

    context = {
        "course_obj": course_obj
    }

    return JsonResponse({"msg": "success", "course_id": course_obj.id,"lesson_ids":[x.title for x in course_obj.lessons.all()]})
    return render(request, "courses/course_detail.html", context)


def lesson_list_view(request, course_id):

    lesson_objects = get_lesson_list(course_id)

    if lesson_objects is None:
        return Http404()

    context = {
        "lesson_obj": lesson_objects
    }
    return JsonResponse({"msg":"success","data":[x.id for x in lesson_objects ]})

    return render(request, "courses/lesson_list.html", context)


def lesson_detail_view(request, course_id, lesson_id):
    lesson_obj = get_lesson_detail(course_id, lesson_id)

    if lesson_obj is None:
        print("this is lesson obj",lesson_obj)
        return JsonResponse({"msg":"not found"})

    context = {
        "lesson_obj": lesson_obj
    }
    return JsonResponse({"msg":"success","lesson_id":lesson_obj.id})
    return render(request, "courses/lesson_detail.html")

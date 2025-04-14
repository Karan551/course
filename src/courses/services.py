from .models import Course, PublishStatus, Lesson


def get_publish_course():
    return Course.objects.filter(status=PublishStatus.PUBLISHED)


def get_course_detail(course_id=None):
    if course_id is None:
        return None

    response = None
    try:
        response = Course.objects.get(
            id=course_id, status=PublishStatus.PUBLISHED)
    except Exception as e:
        print("Error in course detail function::", e)

    return response


def get_lesson_list(course_id=None):

    if not course_id:
        return None

    course = Course.objects.get(id=course_id, status=PublishStatus.PUBLISHED)

    lessons = None
    try:
        lessons = course.lessons.all()

        # IMP --> course.lesson_set.all() uses Django’s reverse relation from Course to Lesson. By default, Django names this as modelname_set (in lowercase), unless you specify a related_name in the ForeignKey.

        # this is another way to the above task
        # lessons = course.lesson_set.all()

    except Exception as e:
        print("Error in lesson list::", e)

    return lessons


def get_lesson_detail(course_id=None, lesson_id=None):

    if not (course_id or lesson_id):
        return None

    lesson = None
    try:
        lesson = Lesson.objects.get(
            course__id=course_id,
            course__status=PublishStatus.PUBLISHED,
            id=lesson_id,
            status=PublishStatus.PUBLISHED
        )
    except Exception as e:
        print("Error in Lesson Detail::", e)
    return lesson

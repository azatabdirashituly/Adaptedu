from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


@api_view(["GET"])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)



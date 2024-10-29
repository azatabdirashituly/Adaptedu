from rest_framework import serializers
from .models import Course, Quiz, Question


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


from rest_framework import serializers
from .models import Course, Topic, Lesson, LessonAccess, LessonSession

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAccess
        fields = '__all__'

class LessonSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonSession
        fields = '__all__'
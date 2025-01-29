from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Course, Topic, Lesson, LessonAccess, LessonSession
from .serializers import (
    CourseSerializer, TopicSerializer, LessonSerializer,
    LessonAccessSerializer, LessonSessionSerializer
)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

class LessonAccessViewSet(viewsets.ModelViewSet):
    queryset = LessonAccess.objects.all()
    serializer_class = LessonAccessSerializer
    permission_classes = [IsAuthenticated]

class LessonSessionViewSet(viewsets.ModelViewSet):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_classes = [IsAuthenticated]
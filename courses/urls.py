from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    CourseViewSet, TopicViewSet, LessonViewSet,
    LessonAccessViewSet, LessonSessionViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'lesson-accesses', LessonAccessViewSet)
router.register(r'lesson-sessions', LessonSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
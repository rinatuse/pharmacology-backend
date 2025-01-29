from django.db import models
from users.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']

class Topic(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.name} - {self.name}"
    
    class Meta:
        ordering = ['id']

class Lesson(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='lessons')
    theory_content = models.TextField()
    test_content = models.TextField()
    lesson_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic.name} - Урок {self.lesson_order}"
    
    class Meta:
        ordering = ['lesson_order']

class LessonAccess(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='accesses')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_accesses')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='granted_accesses')
    is_granted = models.BooleanField(default=False)
    granted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Access to {self.lesson} for {self.student.email}"

class LessonSession(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='sessions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_sessions')
    session_date = models.DateTimeField(auto_now_add=True)
    test_passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - {self.lesson} - {'Passed' if self.test_passed else 'Not passed'}"
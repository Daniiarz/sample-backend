from django.contrib import admin

# Register your models here.
from backend.models import Lesson, Exam, User

admin.site.register(Lesson)
admin.site.register(Exam)
admin.site.register(User)

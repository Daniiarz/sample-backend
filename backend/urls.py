from django.urls import path
from . import views

urlpatterns = [
    path('marks/', views.ListLessonMarkAPIView.as_view()),
    path('presence/', views.ListLessonPresenceAPIView.as_view()),
]

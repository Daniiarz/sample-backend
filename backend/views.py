from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from backend.models import User, Lesson
from backend.serializers import (
    MarkUserSerializer, PresenceUserSerializer, LessonMarkSerializer, LessonPresenceSerializer
)


# Create your views here.


class ListLessonPresenceAPIView(ListCreateAPIView):
    serializer_class = MarkUserSerializer
    queryset = User.objects.prefetch_related("lessons").exclude(type=User.TEACHER)

    def post(self, request, *args, **kwargs):
        serializer = LessonPresenceSerializer(data=request.data)
        serializer.is_valid(True)
        Lesson.objects.filter(id=serializer.data.get("lesson_id")).update(presence=serializer.data["presence"])
        return Response(status=status.HTTP_201_CREATED)


class ListLessonMarkAPIView(ListCreateAPIView):
    serializer_class = PresenceUserSerializer
    queryset = User.objects.prefetch_related("lessons").exclude(type=User.TEACHER)

    def post(self, request, *args, **kwargs):
        serializer = LessonMarkSerializer(data=request.data)
        serializer.is_valid(True)
        Lesson.objects.filter(id=serializer.data.get("lesson_id")).update(mark=serializer.data["mark"])
        return Response(status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

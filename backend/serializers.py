from rest_framework import serializers

from backend.models import User, Lesson


class MarkLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'mark',
        )


class PresenceLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'presence',
        )


class MarkUserSerializer(serializers.ModelSerializer):
    lessons = MarkLessonSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'type',
            'username',
            'first_name',
            'last_name',
            'group',
            'lessons'
        )


class PresenceUserSerializer(serializers.ModelSerializer):
    lessons = PresenceLessonSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'type',
            'username',
            'first_name',
            'last_name',
            'group',
            'lessons',
        )


class LessonMarkSerializer(serializers.Serializer):  # noqa
    mark = serializers.IntegerField()
    lesson_id = serializers.IntegerField()


class LessonPresenceSerializer(serializers.Serializer):  # noqa
    presence = serializers.IntegerField()
    lesson_id = serializers.IntegerField()

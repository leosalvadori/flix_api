from rest_framework import serializers
from actors.models import Actor
from rest_framework.validators import UniqueValidator


class ActorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=200,
        validators=[UniqueValidator(queryset=Actor.objects.all())]
    )

    class Meta:
        model = Actor
        fields = '__all__'

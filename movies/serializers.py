from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from django.db.models import Avg


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('The release date must be greater than 1900-01-01')
        return value


class MovieDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actores = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate_avg = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate_avg:
            return round(rate_avg, 1)

        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    moveis_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()

from movies.models import Movie
from rest_framework import generics, views, response, status
from movies.serializers import MovieSerializer, MovieStatsSerializer, MovieDetailSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissionClass
from django.db.models import Count, Avg
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_movies': total_movies,
            'moveis_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': average_stars
        }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK,
        )

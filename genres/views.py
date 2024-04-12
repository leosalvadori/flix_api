from genres.models import Genre
from rest_framework import generics, viewsets
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from app.permissions import GlobalPermissionClass


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

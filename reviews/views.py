from reviews.models import Review
from rest_framework import generics
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissionClass


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermissionClass]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

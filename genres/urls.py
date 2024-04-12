from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('genrees', views.GenreViewSet, basename='genre_viewset')

urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-details-view'),
]

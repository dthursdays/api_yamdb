from rest_framework import viewsets, mixins, filters
from reviews.models import Category, Genre, Title
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleSerializer, TitleCreateSerialize)
from .permissions import IsAdminOrReadOnly
from django.db.models import Avg


class CreateListDestroyViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    permission_classes = (IsAdminOrReadOnly)
    filter_backends = (filters.SearchFilter)
    search_fields = ('name',)
    lookup_field = 'slug'


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(Avg("reviews__score"))
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly)
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return TitleCreateSerialize
        return TitleSerializer

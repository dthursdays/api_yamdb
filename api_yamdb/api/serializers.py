from rest_framework import serializers

from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.IntegerField(default=None, read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category',)
        read_only_fields = ('__all__')


class TitleCreateSerialize(TitleSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_fields='slug',
        many=True)
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_fields='slug',
        many=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description',
                  'genre', 'category',)

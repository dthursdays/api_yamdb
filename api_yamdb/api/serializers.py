from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title
from django.shortcuts import get_object_or_404


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
        read_only_fields = ('__all__', )


class TitleCreateSerialize(TitleSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
        many=False)
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True)
    description = serializers.CharField(
        required=False
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description',
                  'genre', 'category',)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = (
            'id', 'text',
            'author', 'score', 'pub_date',
        )
        read_only_fields = ('author', )

    def validate_score(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError(
                'Ваша оценка должна быть от 0 до 10'
            )
        return value

    def validate(self, value):
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        author = self.context['request'].user
        if Review.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(
                'Нельзя оставлять отзыв повторно!'
            )
        return value


class ReviewUpdateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = (
            'id', 'text',
            'author', 'score', 'pub_date',
        )
        read_only_fields = ('author', )

    def validate_score(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError(
                'Ваша оценка должна быть от 0 до 10'
            )
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = (
            'id', 'text',
            'author', 'pub_date',
        )
        read_only_fields = ('author',)

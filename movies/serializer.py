from rest_framework import serializers
from .models import Actor, Movie, Review

# 전체 배우 목록
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# 단일 배우 정보 제공 (출연 영화 제목 포함)
class ActorSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title')

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = "__all__"

# 전체 영화 목록
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

# 단일 영화 정보 (출연 배우 이름과 리뷰 목록 포함)
class MovieSerializer(serializers.ModelSerializer):
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    class ReviewListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content')
    actors = ActorSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

# 전체 리뷰 목록
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title',)

# 단일 리뷰 정보 (출연 영화 제목 포함)
class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
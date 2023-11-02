# serializers.py

from rest_framework import serializers
from .models import CustomUser, Category, Tag, Post, Comment


# CustomUser serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'is_active', 'is_staff')


# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


# Tag serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ('content', 'pub_date', 'author', 'post')


# Post serializer
class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'pub_date', 'author', 'category', 'tags', 'comments')

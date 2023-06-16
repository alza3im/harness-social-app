from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "content")

    def create(self, validated_data):
        author = self.context["request"].user  # Get the authenticated user
        instance = self.Meta.model(author=author, **validated_data)
        instance.save()
        return instance

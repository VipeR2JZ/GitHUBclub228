from rest_framework import serializers
from blog.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','author','body']
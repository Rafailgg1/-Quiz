from rest_framework import serializers 
from .models import Tag, Post
from rest_framework.serializers import CurrentUserDefault


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    class Meta:
     model = Tag
     fields = ('id', 'user_id', 'user', 'post',
               'content', 'created_at', 'updated_at' 
               )
     read_only_fields = ('user_id', 'created_at', 'updated_at')
    def user_id(self, obj):
        return obj.user.id

class TagSerializer(serializers.ModelSerializer):
    class Meta:
     model = Tag
     fields = ('id', 'user_id', 'user', 'post',
               'content', 'created_at', 'updated_at' 
               )
     read_only_fields = ('user_id', 'created_at', 'updated_at')
    def user_id(self, obj):
        return obj.user.id
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'ttile', 'description')

class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Post
        fields = (
            'id', 'content', 'topic', 'tags', 'user_id', 'user',
            'crated_at', 'update_at'
            )
        # eclude = ('user',)
        
    def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        # kwargs['user'] = CurrentUserDefault()
        print(kwargs['user'].username)
        return super().save(**kwargs)
    
    def user_id(self, obj):
        return obj.user.id
    
    def tags(self, obj):
        return TagSerializer(obj.tags.all(), many=True).data
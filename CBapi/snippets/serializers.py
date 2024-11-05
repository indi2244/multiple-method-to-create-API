from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User
#creating serializer class
'''class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    code = serializers.CharField()
    linenos = serializers.BooleanField()

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.save()
        return instance'''

#using model serializers
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
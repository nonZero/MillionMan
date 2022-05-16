from rest_framework import serializers

from blog import models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = (
            "id",
            "title",
            "posted_at",
            "teaser",
            "content",
        )


# class ConeSerializer(serializers.Serializer):
#     scoops = serializers.IntegerField()
#     topping = serializers.CharField()
#     has_cream = serializers.BooleanField(default=False)
#     purchased_at = serializers.DateField(required=False)
#     flavours = serializers.ListField(child=serializers.CharField())

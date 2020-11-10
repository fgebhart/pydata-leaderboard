from rest_framework import serializers
from ranking_app.models import Ranking


class RankingSerializer(serializers.Serializer):
    user = serializers.CharField(required=True, max_length=100)
    score = serializers.FloatField()

    def create(self, validated_data):
        return Ranking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.score = validated_data.get('score', instance.score)
        instance.save()
        return instance
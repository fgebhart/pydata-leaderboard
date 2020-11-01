from rest_framework import serializers
from ranking_app.models import Ranking


class RankingSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    user = serializers.CharField(required=True, max_length=100)
    score = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Ranking` instance, given the validated data.
        """
        return Ranking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Ranking` instance, given the validated data.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.score = validated_data.get('score', instance.score)
        instance.save()
        return instance
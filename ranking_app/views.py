from django.shortcuts import render
from django.views.generic import View

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from ranking_app import models
from ranking_app.models import Ranking
from ranking_app.serializers import RankingSerializer


class DashboardView(View):
    template_name = "dashboard.html"

    def get(self, request):
        # get ranking of users ordered by score descending
        ranking = models.Ranking.objects.all().order_by("-score")
        return render(request, template_name=self.template_name, context={"ranking": ranking})

class TableView(View):
    template_name = "table.html"

    def get(self, request):
        # get ranking of users ordered by score descending
        ranking = models.Ranking.objects.all().order_by("-score")
        return render(request, template_name=self.template_name, context={"ranking": ranking})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_score(request):
    if request.method == 'POST':
        serializer = RankingSerializer(data=request.data)
        if serializer.is_valid():
            user_instance = Ranking.objects.filter(user=request.data["user"]).first()
            if user_instance:   # user exists already
                # update the score of the user
                user_instance.score = request.data['score']
                user_instance.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:  # user does not exist already
                serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

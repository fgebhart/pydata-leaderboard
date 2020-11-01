from django.shortcuts import render
from django.views.generic import View

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ranking_app import models
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
def add_user_score(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = RankingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

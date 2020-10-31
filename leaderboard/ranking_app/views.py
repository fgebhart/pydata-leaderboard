from django.shortcuts import render
from django.views.generic import View


from ranking_app import models


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

from django.db import models


class Ranking(models.Model):

    def __str__(self):
        return f"{self.user}: {self.score}"

    user = models.CharField(max_length=100, unique=True)
    score = models.IntegerField()

from ranking_app import models


def test_ranking(db):
    ranking = models.Ranking(user="Player1", score=123)
    ranking.save()
    assert ranking.user == "Player1"
    assert ranking.score == 123
    ranking_object = models.Ranking.objects.get(user="Player1")
    assert ranking_object.user == "Player1"
    assert ranking_object.score == 123
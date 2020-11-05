from django.urls import reverse

from ranking_app import models


def test_dashboard_view(db, client):
    response = client.get(reverse("leaderboard"))
    assert response.status_code == 200
    assert "BlueYonder Beer Game" in response.content.decode("UTF-8")


def test_table_view(db, client):
    ranking = models.Ranking(user="Player1", score=123)
    ranking.save()
    response = client.get(reverse("table"))
    assert response.status_code == 200
    assert "Player1" in response.content.decode("UTF-8")


def test_add_user_score_endpoint(db, client, api_client_with_credentials):
    data = {'user': 'Player2', 'score': 1}
    headers={"content-type": "application/json"},

    # not authorized post request
    response = client.post(path=reverse("add-user-score"), json=data, headers=headers)
    assert response.status_code == 403  # forbidden

    # authorized post request
    response = api_client_with_credentials.post(reverse("add-user-score"), json=data, headers=headers)
    assert response.status_code != 403  # not forbidden


    

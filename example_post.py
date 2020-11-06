import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    
    # authentication
    username = "username"
    password = "password"

    # payload data
    data = {"user": "Player1", "score": 1234}
    
    r = requests.post(
        url="http://127.0.0.1:8000/add-user-score",
        json=data,
        headers={"content-type": "application/json"},
        auth=HTTPBasicAuth(username, password),    
    )

    assert r.ok
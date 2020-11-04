# PyData-Leaderboard
Leaderboard for the Bot Game Challenge of the PyDataGlobal 2020


## Deployment
Build the docker image
```bash
docker build . -t pydata-leaderboard
```
Run the django app
```bash
docker run --rm  -it -p 8000:8000  -v $(pwd):/leaderboard pydata-leaderboard
```


## Updating the Leaderboard
The leaderboard app comes with a dedicated Rest API end point for adding (and updating) scores of users.
To add a new user to the leaderboard simply send a POST similar to the following one to the endpoint `/add-user-score`:

```bash
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"user":"player-name","score":1234}' \
     -u username:password \
     http://127.0.0.1:8000/add-user-score
```

where `http://127.0.0.1:8000` is the url to the leaderboard app.
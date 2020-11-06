from django.contrib.auth.models import User


def create_user(username: str, password: str):
    if not User.objects.filter(name=username).first():
        # user does not yet exist -> create one
        User.objects.create_user(username=username, password=password)

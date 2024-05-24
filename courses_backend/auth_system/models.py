
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
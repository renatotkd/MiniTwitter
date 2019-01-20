from django.db import models
from django.contrib.auth.models import User

from .validators import validate_cpf

class MyUser(User):
    cpf = models.CharField(
        max_length=14,
        validators=[validate_cpf]
    )


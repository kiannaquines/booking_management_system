from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USER_TYPE = [
        ('Client', 'Client'),
        ('Staff', 'Staff'),
        ('Manager', 'Manager'),
        ('Driver', 'Driver'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPE)

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        db_table = 'users'
        verbose_name = 'Users'

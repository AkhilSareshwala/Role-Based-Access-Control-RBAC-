from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("MANAGER", "Manager"),
        ("USER", "User"),
    )
    # require unique emails
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="USER")

    def is_admin(self):
        return self.role == "ADMIN"

    def is_manager(self):
        return self.role == "MANAGER"

    def is_user(self):
        return self.role == "USER"

    def __str__(self):
        return f"{self.email} ({self.role})"

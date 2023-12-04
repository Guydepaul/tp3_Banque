from django.contrib.auth.models import User
from django.db import models

class Compte(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Compte de {self.user.username}"

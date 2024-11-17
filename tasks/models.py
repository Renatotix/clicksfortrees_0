from django.db import models

from django.contrib.auth.models import User

class UserClick(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0)
    trees_planted = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Clicks: {self.clicks}, Trees: {self.trees_planted}"

    def add_click(self):
        self.clicks += 1
        if self.clicks % 10 == 0:  # Por ejemplo, cada 10 clics se planta un árbol
            self.trees_planted += 1
        self.save()
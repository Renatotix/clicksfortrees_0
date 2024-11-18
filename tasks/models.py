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

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    arboles_plantados = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

class Skin(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo_en_arboles = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='skins/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    skin = models.ForeignKey(Skin, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} compró {self.skin.nombre}"
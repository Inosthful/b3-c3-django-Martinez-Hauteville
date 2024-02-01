from django.db import models
from django.conf import settings

class Site(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    identifiant = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.nom

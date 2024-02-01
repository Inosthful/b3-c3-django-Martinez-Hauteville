from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet

CRYPTO_KEY = b'TODO: GENERATE CRYPTO KEY'

class Site(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    identifiant = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , null=True)
    mot_de_passe_chiffre = models.CharField(max_length=255)

    def set_mot_de_passe(self, raw_password):
        f = Fernet(CRYPTO_KEY)
        self.mot_de_passe_chiffre = f.encrypt(raw_password.encode()).decode()

    def get_mot_de_passe(self):
        f = Fernet(CRYPTO_KEY)
        return f.decrypt(self.mot_de_passe_chiffre.encode()).decode()
    
    def __str__(self):
        return self.nom

from django.db import models

# Create your models here.
class Profil(models.Model):
    navn = models.CharField(max_length=100, null=False )
    kallenavn = models.CharField(max_length=100, null=True )
    registrert = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.navn
    
    
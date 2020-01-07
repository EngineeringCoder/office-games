from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Profile(models.Model):
    
    class TrashTalkFactor(models.TextChoices):
        NOOB = 'NO', _('Nybegynner')
    
    
    name = models.CharField(max_length=100, null=False )
    nickname = models.CharField(max_length=100, null=True )
    joined = models.DateTimeField(auto_now_add=True)
    profile_text = models.TextField(null=True)
    trashtalk = models.CharField(max_length=5, choices=TrashTalkFactor.choices, default=TrashTalkFactor.NOOB)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
    
    
from django.db import models

# Create your models here.
class Kamp(models.Model):
    tidspunkt = models.DateTimeField(auto_now_add=True)
    vinner1 = models.ForeignKey(Spiller,on_delete=models.CASCADE,null=False)
    vinner2 = models.ForeignKey(Spiller,on_delete=models.CASCADE)
    taper1 = models.ForeignKey(Spiller,on_delete=models.CASCADE)
    taper2 = models.ForeignKey(Spiller,on_delete=models.CASCADE)


    __str__(self):
        return self.id
    
    # get_absolute_url(self):
        # return reverse("_detail", kwargs={"pk": self.pk})
    
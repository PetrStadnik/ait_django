from django.db import models

# Create your models here.
class Udalost(models.Model):
    jmeno = models.CharField(max_length=150, null=False)
    popis = models.TextField(max_length=500, null=True)
    def __str__(self):
        return str(self.jmeno) + ": ("+ str(self.popis) + ")"
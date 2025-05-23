from datetime import datetime

from django.db import models

# Create your models here.
class Udalost(models.Model):
    jmeno = models.CharField(max_length=150, null=False)
    popis = models.TextField(max_length=500, null=True)
    zacatek = models.DateTimeField(default=datetime.now())
    konec = models.DateTimeField(default=datetime.now())
    jen_zacatek = models.BooleanField(default=False)
    celodenni = models.BooleanField(default=True)
    def __str__(self):
        return str(self.jmeno) + ": ("+ str(self.popis) + ")"

class Ukol(models.Model):
    jmeno = models.CharField(max_length=150, null=False)
    popis = models.TextField(max_length=500, null=True)
    deadline = models.DateTimeField(default=datetime.now())
    splneno = models.BooleanField(default=False)
    udalost = models.ForeignKey(Udalost, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.udalost.jmeno) + " -> " + self.jmeno
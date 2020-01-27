from django.db import models

# Create your models here.
from clients.models import Client


class Portfolio(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default='')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="portfolios")
    last_user = models.CharField(max_length=100, null=True, blank=True, default='')
    id_last_user = models.IntegerField(null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    tasa_honorarios = models.FloatField(blank=True, null=True, default=0)

    def __str__(self):
        return "{} de {}".format(self.name, self.client)

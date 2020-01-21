from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default='')
    last_user = models.CharField(max_length=100, null=True, blank=True, default='')
    id_last_user = models.IntegerField(null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clients'
        verbose_name = "Cliente"

    def __str__(self):
        return self.name

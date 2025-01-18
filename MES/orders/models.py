from django.db import models


class Clients(models.Model):
    client = models.CharField(max_length=350, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Orders(models.Model):
    contract_number = models.PositiveIntegerField()
    id_client = models.ForeignKey(Clients, on_delete=None)
    contract = models.FileField(upload_to='documentation/contracts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

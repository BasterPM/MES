from datetime import date

from django.db import models


class Clients(models.Model):
    client = models.CharField(max_length=350, blank=True, verbose_name='Клиент', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f"{self.client}"


class Orders(models.Model):
    contract_number = models.PositiveIntegerField(verbose_name='Номер договора', unique=True)
    id_client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True, verbose_name='Клиент')
    contract = models.FileField(upload_to='contracts', verbose_name='Файл договора')
    deadline = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.contract_number}, {self.id_client}"

from django.db import models
from ..storehouse import Storehouse
from ..users.models import Employee
from ..orders.models import Orders


class Task(models.Model):
    id_order = models.ForeignKey(Orders,
                                 on_delete=models.CASCADE,
                                 verbose_name='Номер заказа')
    id_storehouse_unit = models.ForeignKey(Storehouse,
                                           on_delete=models.CASCADE,
                                           verbose_name='Наименование изделия')
    quantity = models.IntegerField(verbose_name='Количество')


class ProductionPath(models.Model):
    id_storehouse_unit = models.ForeignKey(Storehouse,
                                           on_delete=models.CASCADE,
                                           verbose_name='Наименование изделия')
    turn = models.IntegerField(verbose_name='очередь операции')
    description = models.CharField(max_length=500, verbose_name='Описание операции')
    id_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, verbose_name='Исполнитель')

from django.db import models
from storehouse.models import Storehouse
from users.models import EmployeePosition
from orders.models import Orders


class StatusTask(models.TextChoices):
    NEW_TASK = 'Новая задача', 'Новая задача'
    AT_WORK = 'В работе', 'В работе'
    COMPLETED = 'Завершено', 'Завершено'
    EXPIRED = 'Просрочено', 'Просрочено'


class Task(models.Model):
    id_order = models.ForeignKey(Orders,
                                 on_delete=models.CASCADE,
                                 verbose_name='Номер заказа')
    id_storehouse_unit = models.ForeignKey(Storehouse,
                                           on_delete=models.CASCADE,
                                           verbose_name='Наименование изделия')
    quantity = models.IntegerField(verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f"{self.id_order}"


class ProductionPath(models.Model):
    id_storehouse_unit = models.ForeignKey(Storehouse,
                                           on_delete=models.CASCADE,
                                           verbose_name='Наименование изделия')
    turn = models.IntegerField(verbose_name='очередь операции')
    description = models.CharField(max_length=500, verbose_name='Описание операции')
    id_employee = models.ForeignKey(EmployeePosition, on_delete=models.SET_NULL, verbose_name='Специалист', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Техпроцесс'
        verbose_name_plural = 'Техпроцессы'

    def __str__(self):
        return f"{self.id_storehouse_unit}"


class HeadOfProductionTask(models.Model):
    id_order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказ')
    status = models.CharField(max_length=50, choices=StatusTask.choices, default=StatusTask.NEW_TASK,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

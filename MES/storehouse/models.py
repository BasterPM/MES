from django.db import models


class MethodObtaining(models.Model):
    # Метод получения
    method_obtaining = models.CharField(max_length=80, unique=True)


class UnitMeasurement(models.Model):
    # количество (шутки, мм)
    unit_measurement = models.CharField(max_length=20, unique=True)


class Storehouse(models.Model):
    # Склад
    storehouse_unit = models.CharField(max_length=150, unique=True)
    id_method_obtaining = models.ForeignKey(MethodObtaining, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    id_unit_measurement = models.ForeignKey(UnitMeasurement, on_delete=models.SET_NULL, null=True)


class FinalProduct(models.Model):
    # Изделие
    id_storehouse_product = models.ForeignKey(Storehouse, on_delete=models.CASCADE)
    id_storehouse_elements = models.ManyToManyField(Storehouse, related_name='product_elements')


class AssemblyUnit(models.Model):
    # Сборочная единица
    id_storehouse_assembly_unit = models.ForeignKey(Storehouse, on_delete=models.CASCADE)
    id_storehouse_elements = models.ManyToManyField(Storehouse, related_name='assembly_unit_elements')


class OwnProduction(models.Model):
    # Собственное производство
    id_storehouse_own_production = models.ForeignKey(Storehouse, on_delete=models.CASCADE)
    id_storehouse_elements = models.ManyToManyField(Storehouse, related_name='own_production_elements')

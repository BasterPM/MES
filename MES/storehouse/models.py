from django.db import models


class MethodObtaining(models.Model):
    # Метод получения
    method_obtaining = models.CharField(max_length=80, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UnitMeasurement(models.Model):
    # количество (шутки, мм)
    unit_measurement = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Seller(models.Model):
    seller_name = models.CharField(max_length=300, unique=True)
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField(max_length=150, blank=True)
    website = models.URLField(blank=True)


class Storehouse(models.Model):
    # Склад
    storehouse_unit = models.CharField(max_length=150, unique=True)  # название
    c1_article = models.IntegerField(blank=True)  # артикул по 1ске
    id_method_obtaining = models.ForeignKey(MethodObtaining, on_delete=models.SET_NULL, null=True)
    # айди способа получения
    quantity = models.IntegerField(default=0)  # количество на складе
    id_unit_measurement = models.ForeignKey(UnitMeasurement, on_delete=models.SET_NULL, null=True)
    # айди меры измерения
    storage_place = models.CharField(max_length=150, blank=True)
    # место хранения
    id_seller = models.ManyToManyField(Seller, related_name='seller', blank=True)  # айди продовца
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FinalProduct(models.Model):
    # Изделие
    id_storehouse_product = models.ForeignKey(Storehouse, on_delete=models.CASCADE)
    id_storehouse_elements = models.ManyToManyField(Storehouse, related_name='product_elements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AssemblyUnit(models.Model):
    # Сборочная единица
    id_storehouse_assembly_unit = models.ForeignKey(Storehouse, on_delete=models.CASCADE)
    id_storehouse_elements = models.ManyToManyField(Storehouse, related_name='assembly_unit_elements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OwnProduction(models.Model):
    # Собственное производство
    id_storehouse_own_production = models.ForeignKey(Storehouse, on_delete=models.CASCADE)
    id_storehouse_elements = models.ManyToManyField(Storehouse, related_name='own_production_elements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TechnologicalProcess(models.Model):
    # Техническая документация на элементы хранения на складе
    id_storehouse_unit = models.ForeignKey(Storehouse, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='documentation/technological_process')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




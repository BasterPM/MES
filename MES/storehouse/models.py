from django.db import models
from MES.users import EmployeePosition


class MethodObtaining(models.Model):
    # Метод получения
    method_obtaining = models.CharField(max_length=80, unique=True, verbose_name='Метод получения')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Метод получения'
        verbose_name_plural = 'Метод получения'

    def __str__(self):
        return f"{self.method_obtaining}"


class UnitMeasurement(models.Model):
    # количество (шутки, мм)
    unit_measurement = models.CharField(max_length=20, unique=True, verbose_name='Мера измерения')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Количество'
        verbose_name_plural = 'Количество'

    def __str__(self):
        return f"{self.unit_measurement}"


class Seller(models.Model):
    seller_name = models.CharField(max_length=300, unique=True, verbose_name='Продавец')
    phone_number = models.IntegerField(blank=True, verbose_name='Телефонный номер продовца')
    email = models.EmailField(max_length=150, blank=True, verbose_name='почта продовца')
    website = models.URLField(blank=True, verbose_name='Сайт продовца')

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return f"{self.seller_name}"


class Storehouse(models.Model):
    # Склад
    storehouse_unit = models.CharField(max_length=150, unique=True, verbose_name='Наименование')  # название
    c1_article = models.IntegerField(blank=True, verbose_name='Артикул в 1С')  # артикул по 1ске
    # айди способа получения
    id_method_obtaining = models.ForeignKey(MethodObtaining,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            verbose_name='Спопоб получания')
    quantity = models.IntegerField(default=0, verbose_name='Количество')  # количество на складе
    # айди меры измерения
    id_unit_measurement = models.ForeignKey(UnitMeasurement,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            verbose_name='Мера измерения')
    # место хранения
    storage_place = models.CharField(max_length=150, blank=True, verbose_name='Место хранения')
    # айди продовца
    id_seller = models.ManyToManyField(Seller, related_name='seller', blank=True, verbose_name='Продавец')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'

    def __str__(self):
        return f"{self.storehouse_unit}"


class FinalProduct(models.Model):
    # Изделие
    id_storehouse_product = models.ForeignKey(Storehouse, on_delete=models.CASCADE, verbose_name='Изделие')
    id_storehouse_elements = models.ManyToManyField(Storehouse,
                                                    related_name='product_elements',
                                                    verbose_name='Составные части изделия')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    id_unit_measurement = models.ForeignKey(UnitMeasurement,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            verbose_name='Мера измерения')
    id_employee_position = models.ManyToManyField(EmployeePosition,
                                                  related_name='employee_position',
                                                  verbose_name='Специализация исполнителя')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'

    def __str__(self):
        return f"{self.id_storehouse_product}"


class AssemblyUnit(models.Model):
    # Сборочная единица
    id_storehouse_assembly_unit = models.ForeignKey(Storehouse,
                                                    on_delete=models.CASCADE,
                                                    verbose_name='Сборочная единица')
    id_storehouse_elements = models.ManyToManyField(Storehouse,
                                                    related_name='assembly_unit_elements',
                                                    verbose_name='Составные части сборочной единицы')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    id_unit_measurement = models.ForeignKey(UnitMeasurement,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            verbose_name='Мера измерения')
    id_employee_position = models.ManyToManyField(EmployeePosition,
                                                  related_name='employee_position',
                                                  verbose_name='Специализация исполнителя')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сборочная единица'
        verbose_name_plural = 'Сборочные единицы'

    def __str__(self):
        return f"{self.id_storehouse_assembly_unit}"


class OwnProduction(models.Model):
    # Собственное производство
    id_storehouse_own_production = models.ForeignKey(Storehouse,
                                                     on_delete=models.CASCADE,
                                                     verbose_name='Элемент собственного производства')
    id_storehouse_elements = models.ManyToManyField(Storehouse,
                                                    related_name='own_production_elements',
                                                    verbose_name='Материал')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    id_unit_measurement = models.ForeignKey(UnitMeasurement,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            verbose_name='Мера измерения')
    id_employee_position = models.ManyToManyField(EmployeePosition,
                                                  related_name='employee_position',
                                                  verbose_name='Специализация исполнителя')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Элемент собственного производства'
        verbose_name_plural = 'Элементы собственного производства'

    def __str__(self):
        return f"{self.id_storehouse_own_production}"


class TechnologicalProcess(models.Model):
    # Техническая документация на элементы хранения на складе
    id_storehouse_unit = models.ForeignKey(Storehouse,
                                           on_delete=models.CASCADE,
                                           verbose_name='Элемент склада')
    pdf_file = models.FileField(upload_to='technological_process',
                                verbose_name='Файл с технической документацией')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Техническая документация '
        verbose_name_plural = 'Техническая документация'

    def __str__(self):
        return f"{self.id_storehouse_unit}"

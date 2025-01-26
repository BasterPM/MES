from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class EmployeePosition(models.Model):
    position = models.CharField(max_length=100, unique=True, verbose_name='Специализация')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return f"{self.position}"


class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True, verbose_name='Должность')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return f"{self.role_name}"


class Employee(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    position = models.ManyToManyField(EmployeePosition,
                                      related_name='employees',
                                      blank=True,
                                      verbose_name='Специализация')
    role = models.ForeignKey(Role,
                             related_name='role',
                             blank=True,
                             verbose_name='Должность',
                             on_delete=models.SET_NULL,
                             null=True)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.role}, {self.position}"

#
# class Clients(models.Model):
#     client = models.CharField(max_length=350, blank=True, verbose_name='Клиент')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Клиент'
#         verbose_name_plural = 'Клиенты'
#
#     def __str__(self):
#         return f"{self.client}"
#
#
# class Orders(models.Model):
#     contract_number = models.PositiveIntegerField(verbose_name='Номер договора')
#     id_client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True, verbose_name='Клиент')
#     contract = models.FileField(upload_to='contracts', verbose_name='Файл договора')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#     def __str__(self):
#         return f"{self.contract_number}, {self.id_client}"
#
#
# class MethodObtaining(models.Model):
#     # Метод получения
#     method_obtaining = models.CharField(max_length=80, unique=True, verbose_name='Метод получения')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Метод получения'
#         verbose_name_plural = 'Метод получения'
#
#     def __str__(self):
#         return f"{self.method_obtaining}"
#
#
# class UnitMeasurement(models.Model):
#     # количество (шутки, мм)
#     unit_measurement = models.CharField(max_length=20, unique=True, verbose_name='Мера измерения')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Количество'
#         verbose_name_plural = 'Количество'
#
#     def __str__(self):
#         return f"{self.unit_measurement}"
#
#
# class Seller(models.Model):
#     seller_name = models.CharField(max_length=300, unique=True, verbose_name='Продавец')
#     phone_number = models.IntegerField(blank=True, verbose_name='Телефонный номер продовца')
#     email = models.EmailField(max_length=150, blank=True, verbose_name='почта продовца')
#     website = models.URLField(blank=True, verbose_name='Сайт продовца')
#
#     class Meta:
#         verbose_name = 'Продавец'
#         verbose_name_plural = 'Продавцы'
#
#     def __str__(self):
#         return f"{self.seller_name}"
#
#
# class Storehouse(models.Model):
#     # Склад
#     storehouse_unit = models.CharField(max_length=150, unique=True, verbose_name='Наименование')  # название
#     c1_article = models.IntegerField(blank=True, verbose_name='Артикул в 1С')  # артикул по 1ске
#     # айди способа получения
#     id_method_obtaining = models.ForeignKey(MethodObtaining,
#                                             on_delete=models.SET_NULL,
#                                             null=True,
#                                             verbose_name='Спопоб получания')
#     quantity = models.IntegerField(default=0, verbose_name='Количество')  # количество на складе
#     # айди меры измерения
#     id_unit_measurement = models.ForeignKey(UnitMeasurement,
#                                             on_delete=models.SET_NULL,
#                                             null=True,
#                                             verbose_name='Мера измерения')
#     # место хранения
#     storage_place = models.CharField(max_length=150, blank=True, verbose_name='Место хранения')
#     # айди продовца
#     id_seller = models.ManyToManyField(Seller, related_name='seller', blank=True, verbose_name='Продавец')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Склад'
#         verbose_name_plural = 'Склад'
#
#     def __str__(self):
#         return f"{self.storehouse_unit}"
#
#
# class FinalProduct(models.Model):
#     # Изделие
#     id_storehouse_product = models.ForeignKey(Storehouse, on_delete=models.CASCADE, verbose_name='Изделие')
#     id_storehouse_elements = models.ManyToManyField(Storehouse,
#                                                     related_name='product_elements',
#                                                     verbose_name='Составные части изделия')
#     quantity = models.IntegerField(default=0, verbose_name='Количество')
#     id_unit_measurement = models.ForeignKey(UnitMeasurement,
#                                             on_delete=models.SET_NULL,
#                                             null=True,
#                                             verbose_name='Мера измерения')
#     id_employee_position = models.ManyToManyField(EmployeePosition,
#                                                   related_name='employee_position_final_product',
#                                                   verbose_name='Специализация исполнителя')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Изделие'
#         verbose_name_plural = 'Изделия'
#
#     def __str__(self):
#         return f"{self.id_storehouse_product}"
#
#
# class AssemblyUnit(models.Model):
#     # Сборочная единица
#     id_storehouse_assembly_unit = models.ForeignKey(Storehouse,
#                                                     on_delete=models.CASCADE,
#                                                     verbose_name='Сборочная единица')
#     id_storehouse_elements = models.ManyToManyField(Storehouse,
#                                                     related_name='assembly_unit_elements',
#                                                     verbose_name='Составные части сборочной единицы')
#     quantity = models.IntegerField(default=0, verbose_name='Количество')
#     id_unit_measurement = models.ForeignKey(UnitMeasurement,
#                                             on_delete=models.SET_NULL,
#                                             null=True,
#                                             verbose_name='Мера измерения')
#     id_employee_position = models.ManyToManyField(EmployeePosition,
#                                                   related_name='employee_position_assembly_unit',
#                                                   verbose_name='Специализация исполнителя')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Сборочная единица'
#         verbose_name_plural = 'Сборочные единицы'
#
#     def __str__(self):
#         return f"{self.id_storehouse_assembly_unit}"
#
#
# class OwnProduction(models.Model):
#     # Собственное производство
#     id_storehouse_own_production = models.ForeignKey(Storehouse,
#                                                      on_delete=models.CASCADE,
#                                                      verbose_name='Элемент собственного производства')
#     id_storehouse_elements = models.ManyToManyField(Storehouse,
#                                                     related_name='own_production_elements',
#                                                     verbose_name='Материал')
#     quantity = models.IntegerField(default=0, verbose_name='Количество')
#     id_unit_measurement = models.ForeignKey(UnitMeasurement,
#                                             on_delete=models.SET_NULL,
#                                             null=True,
#                                             verbose_name='Мера измерения')
#     id_employee_position = models.ManyToManyField(EmployeePosition,
#                                                   related_name='employee_position_own_production',
#                                                   verbose_name='Специализация исполнителя')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Элемент собственного производства'
#         verbose_name_plural = 'Элементы собственного производства'
#
#     def __str__(self):
#         return f"{self.id_storehouse_own_production}"
#
#
# class TechnologicalProcess(models.Model):
#     # Техническая документация на элементы хранения на складе
#     id_storehouse_unit = models.ForeignKey(Storehouse,
#                                            on_delete=models.CASCADE,
#                                            verbose_name='Элемент склада')
#     pdf_file = models.FileField(upload_to='technological_process',
#                                 verbose_name='Файл с технической документацией')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Техническая документация '
#         verbose_name_plural = 'Техническая документация'
#
#     def __str__(self):
#         return f"{self.id_storehouse_unit}"
#
#     class Task(models.Model):
#         id_order = models.ForeignKey(Orders,
#                                      on_delete=models.CASCADE,
#                                      verbose_name='Номер заказа')
#         id_storehouse_unit = models.ForeignKey(Storehouse,
#                                                on_delete=models.CASCADE,
#                                                verbose_name='Наименование изделия')
#         quantity = models.IntegerField(verbose_name='Количество')
#
#     class ProductionPath(models.Model):
#         id_storehouse_unit = models.ForeignKey(Storehouse,
#                                                on_delete=models.CASCADE,
#                                                verbose_name='Наименование изделия')
#         turn = models.IntegerField(verbose_name='очередь операции')
#         description = models.CharField(max_length=500, verbose_name='Описание операции')
#         id_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, verbose_name='Исполнитель', null=True)
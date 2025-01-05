from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Employee, EmployeePosition


class UserModelTests(TestCase):
    def test_create_user(self):
        user = Employee.objects.create_user(
            email='test@example.com',
            first_name='Test',
            last_name='User',
            password='securepassword'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertTrue(user.check_password('securepassword'))


class EmployeePositionModelTests(TestCase):
    def test_create_employee_position(self):
        # Создаем позицию
        position = EmployeePosition.objects.create(position='Developer')
        # Проверяем на соответсвия названия
        self.assertEqual(position.position, 'Developer')
        # Проверяем что создалась одна запись в таблице
        self.assertEqual(EmployeePosition.objects.count(), 1)


class UserPositionRelationTests(TestCase):
    def test_user_position_relation(self):
        # Создаем сотрудника
        employee = Employee.objects.create_user(
            email='test@example.com',
            first_name='Test',
            last_name='User',
            password='securepassword'
        )
        # Создаем позицию
        position = EmployeePosition.objects.create(position='Developer')
        # Связываем сотрудника и позицию
        employee.position.add(position)

        self.assertIn(position, employee.position.all())
        self.assertIn(employee, position.employees.all())


class EmployeePositionTestCase(TestCase):
    def setUp(self):
        # Создаем первую позицию
        EmployeePosition.objects.create(position='Developer')

    def test_create_duplicate_employee_position(self):
        # Проверяем, что создание дубликата вызывает ValidationError
        with self.assertRaises(ValidationError):
            position = EmployeePosition(position='Developer')
            position.full_clean()

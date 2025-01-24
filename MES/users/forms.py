from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import Employee


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Employee
        fields = ('email', 'password')

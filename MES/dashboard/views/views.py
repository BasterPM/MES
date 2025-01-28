from django.shortcuts import render, HttpResponse


def dashboard_view(request):
    dashboard_menu = {1: 'manager/main_page.html',  # менеджер
                      2: 'accountant/main_page.html',  # бухгалтер
                      3: 'head_of_production/main_page.html',  # начальник производства
                      4: 'warehouse_worker/main_page.html',  # работник склада
                      5: 'production_worker/main_page.html',  # работник производства
                      6: 'technical_worker/main_page.html'}  # технический работник
    user_role = request.user.role_id
    return render(request, dashboard_menu[user_role])


def my_tasks_view(request):
    return HttpResponse('тут покажем все задачи пользователя')

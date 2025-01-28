from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from orders.forms import OrdersForm, ClientForm
from orders.models import Orders
from task_manager.models import HeadOfProductionTask


def add_order_view(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            id_order = Orders.objects.get(contract_number=request.POST['contract_number'])
            HeadOfProductionTask.objects.create(id_order=id_order)
            return redirect('dashboard')
        else:
            return render(request, 'manager/add_order.html', {'form': form})
    else:
        form = OrdersForm()

    return render(request, 'manager/add_order.html', {'form': form})


    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)  # авторизуем пользователя после регистрации
    #         return redirect('dashboard')  # Перенаправление в личный кабинет
    # else:
    #     form = CustomUserCreationForm()
    # return render(request, 'register.html', {'form': form})


def add_client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'manager/add_client.html', {'form': form})
    else:
        form = ClientForm()

    return render(request, 'manager/add_client.html', {'form': form})


def all_order_view(request):
    search_query = request.GET.get('search', '')
    orders = Orders.objects.all()

    if search_query:
        orders = orders.filter(contract_number__icontains=search_query)

    context = {
        'orders': orders,
        'search_query': search_query,
    }
    return render(request, 'manager/all_order.html', context)


def order_view(request, id):
    # Разобраться и доработать изменение заказа
    order = get_object_or_404(Orders, pk=id)
    data = {
        'contract_number': order.contract_number,
        'id_client': order.id_client,
        'contract': order.contract,
        'deadline': order.deadline,
    }
    form = OrdersForm(data=data)
    if request.method == 'POST':
        # form = OrdersForm(request.POST, request.FILES)
        if form.is_valid():
            data = {
                'contract_number': form.contract_number,
                'id_client': form.id_client,
                'contract': form.contract,
                'deadline': form.deadline,
            }
            order.update(data)
            return redirect('dashboard/all_order')
        else:
            return render(request, 'manager/order.html', {'form': form})
    else:
        return render(request, 'manager/order.html', {'form': form})


def tasks_view(request):
    return HttpResponse('Ваши задачи')

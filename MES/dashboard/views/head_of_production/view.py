from django.shortcuts import render, redirect, HttpResponse


def add_product_view(request):
    return HttpResponse('тут создавать будем конечное изделие')


def add_assembly_view(request):
    return HttpResponse('тут создавать будем сборочную единицу')


def add_own_product_view(request):
    return HttpResponse('тут создавать будем элемент собственного производства')


def add_store_house_element_view(request):
    return HttpResponse('тут создавать будем покупной элемент')


def add_task_view(request):
    return HttpResponse('тут создавать будем задачи')

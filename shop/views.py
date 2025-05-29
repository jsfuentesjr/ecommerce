from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm
from store.models import Product, Category
from django.http import HttpResponse

# Create your views here.


def manage_shop(request):
    return render(request, 'shop/crud.html')


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage-shop')

    context = {'form': form}
    return render(request, 'shop/add-category.html', context)


def update_category(request, pk):

    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('manage-shop')

    context = {'form': form}
    return render(request, 'shop/add-category.html', context)

def delete_category(request, pk):

    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('manage-shop')

    context = {'item':category}
    return render(request, 'shop/delete-category.html', context)


def add_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage-shop')
        else:
            form = ProductForm()

    context = {'form': form}
    return render(request, 'shop/add-product.html', context)

 

    
        

def update_product(request, pk):

    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage-shop')

    context = {'form': form}
    return render(request, 'shop/add-product.html', context)

def delete_product(request, pk):

    prod = Product.objects.get(id=pk)

    if request.method == 'POST':
        prod.delete()
        return redirect('manage-shop')

    context = {'prod':prod}
    return render(request, 'shop/delete-product.html', context)







    
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Designer


def all_products(request):
    """ A view displaying all the products, also includes sorting and search queries """

    products = Product.objects.all()
    categories = Category.objects.all()
    designers = Designer.objects.all()
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'designer' in request.GET:
            designers = request.GET['designer'].split(',')
            products = [product for product in products if product.designer == designers[0]]
            designers = Designer.objects.filter(name__in=designers)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(designer__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'categories': categories,
        'designers': designers,
        'search_term': query,
        'current_categories': categories,


    }

    return render(request, 'products/products.html', context)


def single_product(request, product_id):
    """ A view displaying details of a single product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/single_product.html', context)

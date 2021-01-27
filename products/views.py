from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if "category" in request.GET:
            categories = request.GET['category']
            products = products.filter(category__id__in=categories)
            categories = Category.objects.filter(id__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Type something in the search box")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(
                    description__icontains=query) | Q(
                        material__icontains=query) | Q(
                            brand__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        'current_categories': categories,
    }
    return render(request, "products/all-products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "products/product-detail.html", context)

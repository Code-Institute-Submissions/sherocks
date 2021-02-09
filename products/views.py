from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
import random


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    get_category = None
    get_category_id = None

    if request.GET:

        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET['category']
            products = products.filter(category__id__in=categories)
            categories = Category.objects.filter(id__in=categories)
            category_list = list(categories.values())
            get_category = category_list[0]["friendly_name"]
            get_category_id = category_list[0]["id"]

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

    current_sorting = f"{sort}_{direction}"
    get_category_name = get_category
    category_id = get_category_id

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
        "category_name": get_category_name,
        "category_id": category_id,
    }

    return render(request, "products/all-products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    products = list(Product.objects.all())

    products = random.sample(products, 3)
    first_product = products[0]
    second_product = products[1]
    third_product = products[2]

    product_id = product.id

    reviews = product.reviewed_item.all()

    context = {
        "product": product,
        "first_product": first_product,
        "second_product": second_product,
        "third_product": third_product,
        "reviews": reviews,
    }
    return render(request, "products/product-detail.html", context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Great! Product added.')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Check your form.')
    else:
        form = ProductForm()
    template = "products/add-product.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Great! Product updated.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Check your form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Now editing {product.name}')

    template = "products/edit-product.html"
    context = {
        "form": form,
        "product": product,
    }
    return render(request, template, context)

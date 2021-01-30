from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from products.models import Product
from django.contrib import messages


# Create your views here.
def view_bag(request):
    return render(request, "shopping/shopping-bag.html")


def add_to_bag(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated {size.upper()}to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'You just added {product.name}, {size.upper()}')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'You just added {product.name}, {size.upper()}')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Nice! You added more pieces of {product.name}')
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'You just added {product.name} to your shopping bag')

    request.session["bag"] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
            messages.success(
                    request, f'Updated "{product.name}" in size {size.upper()} to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop()
                messages.success(
                    request, f'Removed "{product.name}", {size.upper()}')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated "{product.name}" quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed "{product.name}" from your shopping bag')

    request.session["bag"] = bag
    return redirect(reverse('shopping'))


def remove_item(request, item_id):
    product = Product.objects.get(pk=item_id)
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f'Removed "{product.name}", {size.upper()} from your shopping bag')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed "{product.name}" from your shopping bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'Something went wrong removing "{product.name}"')
        return HttpResponse(status=500)

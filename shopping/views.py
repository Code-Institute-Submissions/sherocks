from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from products.models import Product
from django.contrib import messages


# View that renders the shopping bag page
def view_bag(request):
    return render(request, "shopping/shopping-bag.html")


# View that allows to add products to the shopping bag
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
                    request, f'Updated size {size.upper()} \
                        for {product.name} to \
                            {bag[item_id]["items_by_size"][size]} items')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'You just added \
                        {product.name}, size {size.upper()}')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'You just added {product.name}, size {size.upper()}')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Nice! You added more \
                    {product.name} to your shopping bag')
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'You just added {product.name} to your shopping bag')

    request.session["bag"] = bag
    return redirect(redirect_url)


# View that allows to update products in the shopping bag
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
            messages.success(request, f'Updated "{product.name}" \
                in size {size.upper()} to \
                    {bag[item_id]["items_by_size"][size]} items')
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop()
            messages.success(request, f'Removed \
                "{product.name}", size {size.upper()}')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated \
                "{product.name}" quantity to {bag[item_id]} items')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed "{product.name}" from your shopping bag')

    request.session["bag"] = bag
    return redirect(reverse('shopping'))


# View that allows to remove products form the shopping bag
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
                    request, f'Removed "{product.name}", \
                        size {size.upper()} from your shopping bag')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed "{product.name}" from your shopping bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'Something went wrong while removing item: {e}"')
        return HttpResponse(status=500)

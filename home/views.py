from django.shortcuts import render
from products.models import Product
import random


# Create your views here.
def index(request):
    get_list = Product.objects.all()

    last_item = get_list.order_by('-id')[:1]
    list_details = last_item.values()
    get_id_item = list_details[0]["id"]
    get_name_item = list_details[0]["name"]
    get_image_item = list_details[0]["image"]
    get_brand_item = list_details[0]["brand"]

    products = list(get_list)

    products = random.sample(products, 3)
    first_product = products[0]
    second_product = products[1]
    third_product = products[2]

    context = {
        "last_id": get_id_item,
        "last_name": get_name_item,
        "last_image": get_image_item,
        "last_brand": get_brand_item,
        "first_product": first_product,
        "second_product": second_product,
        "third_product": third_product,
    }
    return render(request, "home/index.html", context)

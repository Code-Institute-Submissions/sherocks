from django.shortcuts import render
from products.models import Product


# Create your views here.
def index(request):
    get_list = Product.objects.all()
    last_item = get_list.order_by('-id')[:1]
    list_details = last_item.values()
    get_id_item = list_details[0]["id"]
    get_name_item = list_details[0]["name"]
    get_image_url_item = list_details[0]["image_url"]
    get_brand_item = list_details[0]["brand"]
    context = {
        "last_id": get_id_item,
        "last_name": get_name_item,
        "last_image": get_image_url_item,
        "last_brand": get_brand_item,
    }
    print(context)
    return render(request, "home/index.html", context)


import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order
from django.db.models import Q, Count, F
from populate_db import populate_model_with_data

# Create and run your queries within functions

def get_profiles(search_string=None):
    if search_string is None:
        return ''
    query_full_name = Q(full_name__icontains=search_string)
    query_email = Q(email__icontains=search_string)
    query_phone_number = Q(phone_number__icontains=search_string)

    profiles = (Profile.objects.annotate(num_profile_orders=Count('profile_orders'))
                .filter(query_full_name | query_email | query_phone_number)
                .order_by("full_name"))
    if not profiles:
        return ''

    result = []
    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, email: {profile.email}, "
                      f"phone number: {profile.phone_number}, orders: {profile.num_profile_orders}")

    return "\n".join(result)

def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ''
    result = [f"Profile: {profile.full_name}, orders: {profile.num_of_orders}" for profile in profiles]

    return "\n".join(result)

def get_last_sold_products():
    last_order = Order.objects.all().last()
    # products = last_order.products.all().order_by("name")

    if last_order is None or not last_order.products.exists():
        return ""
    # list_of_products = ", ".join(product.name for product in products)
    # return f'Last sold products: {list_of_products}'
    product_names = [product.name for product in last_order.products.all()]

    return f"Last sold products: {', '.join(product_names)}"

def get_top_products():
    top_products = (Product.objects
                    .annotate(num_of_orders=Count('products_orders'))
                    .filter(num_of_orders__gt=0)
                    .order_by("-num_of_orders", "name"))[:5]
    if not top_products:
        return ""

    result = ["Top products:"]
    for product in top_products:
        result.append(f"{product.name}, sold {product.num_of_orders} times")
    return "\n".join(result)

def apply_discounts():
    orders = Order.objects.filter(products__gt=2).filter(is_completed=False)

    num_of_updated_orders = orders.update(total_price=F('total_price') * 0.9)

    return f"Discount applied to {num_of_updated_orders} orders."


def complete_order():
    first_order = Order.objects.filter(is_completed=False).order_by("creation_date").first()

    if not first_order:
        return ""
    products = first_order.products.all()

    for product in products:
        product.in_stock -= 1
        if product.in_stock == 0:
            product.is_available = False
        product.save()

    first_order.is_completed = True
    first_order.save()

    return "Order has been completed!"


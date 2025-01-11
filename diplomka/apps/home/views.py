from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from . import models
from .forms import ReviewForm
from .models import ProductGallery
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', context)

def go_register(request):
    return render(request, 'goreg.html')

def shop(request, category_name=None):
    categories = models.Category.objects.all()
    products = models.Product.objects.all()

    if category_name:
        category = get_object_or_404(models.Category, slug=category_name)
        products = products.filter(category=category)
    else:
        category = None

    context = {
        'categories': categories,
        'products': products,
        'current_category': category,
    }

    return render(request, 'shop.html', context)

def detail_page(request, pk):
        product = get_object_or_404(models.Product, pk=pk)
        related_products = models.Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
        image= ProductGallery.objects.filter(product=product)
        reviews = models.Review.objects.filter(product=product)

        if request.method == 'POST':
            form = ReviewForm(data=request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.product = product
                form.save()
                return redirect('detail', pk=product.pk)

        else:
            form = ReviewForm()

        context = {
            'product': product,
            'related_products':related_products,
            'image':image,
            'reviews': reviews,
            "form":form
        }

        return render(request, 'detail.html', context)


def cart(request):
    # cart_items = models.CartItem.objects.filter(user=request.user)
    # cart_total = sum(item.total_price() for item in cart_items)
    # context = {
    #     'cart_items': cart_items,
    #     'cart_total': cart_total,
    # }
    return render(request, 'cart.html')


def add_to_cart(request, product_id, user_id):
    user = User.objects.get(pk=user_id)
    product = models.Product.objects.get(pk=product_id)

    cart, created = models.Cart.objects.get_or_create(
        user=user
    )

    item, item_created = models.CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    return redirect('cart')

def del_from_cart(request, cart_item_id):
    cart_item = models.CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')



def category_list(request):
    categories = models.Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)

# def review(request, product_id):
#     reviews = models.Review.objects.get(pk=product_id)
#     context = {
#         'reviews': reviews
#     }
#     return render(request, 'detail.html', context)
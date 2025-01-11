from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from . import models
from .forms import ReviewForm
from .models import ProductGallery
from django.core.paginator import Paginator



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

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'page_obj': page_obj,
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
            "form": form,
            'user': request.user
        }

        return render(request, 'detail.html', context)


def cart(request):
    cart = models.Cart.objects.get(user=request.user)
    total_quantity = sum(item.quantity for item in cart.cart_item.all())
    total_sum = sum(item.total_price() for item in cart.cart_item.all())
    context = {
        'cart': cart,
        'total_quantity': total_quantity,
        'total_sum': total_sum,
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    cart, created = models.Cart.objects.get_or_create(user=request.user)

    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))  # Получаем количество из формы
        item, item_created = models.CartItem.objects.get_or_create(cart=cart, product=product)
        if not item_created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

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

def review(request):
    return render(request, 'thanks.html')

# def review(request, product_id):
#     reviews = models.Review.objects.get(pk=product_id)
#     context = {
#         'reviews': reviews
#     }
#     return render(request, 'detail.html', context)
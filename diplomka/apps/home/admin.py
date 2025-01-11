from django.contrib import admin
from .models import Category, Product, CartItem, Review, Favorite, Cart,ProductGallery

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class ProductGalleryInline(admin.StackedInline):
    model = ProductGallery
    min_num = 1
    max_num = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'added_at', 'purchases','display_gallery_images')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('-added_at',)
    readonly_fields = ('added_at',)
    inlines = [ProductGalleryInline]

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price')
    search_fields = ('cart__user__username', 'product__name')
    list_filter = ('product__name',)
    readonly_fields = ('total_price',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'content')
    list_filter = ('rating', 'product')
    search_fields = ('user__username', 'product__name')

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('product__name',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Cart, CartAdmin)


from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='category/image', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Жанр', related_name='products',
                                 null=True, blank=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='product/image', blank=True, null=True)
    added_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    purchases = models.PositiveIntegerField(verbose_name='Кол-во Покупок', default=0)
    price = models.FloatField(verbose_name='Стоимость', default=0.0)

    def __str__(self):
        return self.name

    def display_gallery_images(self):
        photos = self.productgallery_set.all()
        photos_block_start = '<div style="display: flex; gap: 30px">'
        photos_block_end = '</div>'
        images_tags = ''

        for image in photos:
            images_tags += f'<img src="{image.image.url}" width="70" height="70">'
        result = photos_block_start + images_tags + photos_block_end
        return mark_safe(result)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


def product_gallery_image_path(instance, filename):
    return f'product-{instance.product.id}/gallery/{filename}'


# post-2/gallery/post-1.jpg

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Пост')
    image = models.ImageField(upload_to=product_gallery_image_path, verbose_name='Фото')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items',
                             verbose_name='Пользователь')
    products = models.ManyToManyField(
        Product,
        through='CartItem'
    )

    def __str__(self):
        return f"Cart of {self.user.username}"
    class Meta:
        verbose_name='Корзина пользователя'
        verbose_name_plural='Корзины пользователя'

class CartItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cart_item',
        null=True,
        blank=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_item',
        null=True,
        blank=True)
    quantity = models.PositiveIntegerField(default=1)
    is_in_cart = models.BooleanField(default=False, verbose_name='стасус')

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    @property
    def total_price(self):
        return self.product.price * self.quantity


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    content = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    added_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)

    def __str__(self):
        return f'Review-{self.product}: {self.user}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
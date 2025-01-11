from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UserPrюмуofile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='profile'
    )
    image = models.ImageField(
        verbose_name='Аватар',
        upload_to='profiles/avatars/',
        null=True,
        blank=True
    )
    buys_qty = models.PositiveIntegerField(
        verbose_name='Кол-во  покупок',
        default=0
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
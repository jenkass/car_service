from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class AdvUser(AbstractUser):

    def delete(self, *args, **kwargs):
        for bb in self.order_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass


class Cat(models.Model):
    title = models.CharField(max_length=40, unique=True, verbose_name='Услуга')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(default=0, validators=[MaxValueValidator(9999.99), MinValueValidator(1)],
                              verbose_name='Цена')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-created_at']


class Order(models.Model):
    category = models.ForeignKey('Cat', on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey('AdvUser', on_delete=models.CASCADE, verbose_name='Заказ')
    date = models.DateTimeField(unique=True, verbose_name='Дата и время заказа')
    number = models.CharField(max_length=20, verbose_name='Ваш номер')
    is_active = models.BooleanField(default=False, db_index=True, verbose_name='Активировать бронь')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ['-date']

    def __str__(self):
        return self.number

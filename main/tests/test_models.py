from django.test import TestCase
from main.models import *


class CatModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cat.objects.create(title="Шиномонтаж", content='СТО обслуживает идеально', price=2500.55, is_active=True)

    def setUp(self) -> None:
        self.cat = Cat.objects.get(id=1)

    def test_title_label(self):
        field_label = self.cat._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Услуга')

    def test_title_max_length(self):
        max_length = self.cat._meta.get_field('title').max_length
        self.assertEquals(max_length, 40)

    def test_object_name_is_title_comma_title(self):
        expected_object_name = self.cat.title
        self.assertEquals(expected_object_name, str(self.cat))

    def test_title_unique(self):
        unique = self.cat._meta.get_field('title').unique
        self.assertTrue(unique)

    def test_content_label(self):
        field_label = self.cat._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_price_label(self):
        field_label = self.cat._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'Цена')

    def test_price_default(self):
        default = self.cat._meta.get_field('price').default
        self.assertEquals(default, 0)

    def test_is_active_label(self):
        field_label = self.cat._meta.get_field('is_active').verbose_name
        self.assertEquals(field_label, 'Выводить в списке?')

    def test_is_active_default(self):
        default = self.cat._meta.get_field('is_active').default
        self.assertTrue(default)

    def test_created_at_label(self):
        field_label = self.cat._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label, 'Опубликовано')

    def test_created_at_auto_now_add(self):
        date = self.cat._meta.get_field('created_at').auto_now_add
        self.assertTrue(date)


class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cat = Cat.objects.create(title="Шиномонтаж", content='СТО обслуживает идеально', price=2500.55, is_active=True)
        author = AdvUser.objects.create(password='mikipiki123', username='jenkass_')
        Order.objects.create(category=cat, author=author, date='2015-10-12 15:42:22', number='+375299370205')

    def setUp(self) -> None:
        self.order = Order.objects.get(id=1)

    def test_category_label(self):
        field_label = self.order._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'Категория')

    def test_object_name_is_category_comma_title(self):
        expected_object_name = self.order.number
        self.assertEquals(expected_object_name, str(self.order))

    def test_author_label(self):
        field_label = self.order._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'Заказ')

    def test_date_label(self):
        field_label = self.order._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'Дата и время заказа')

    def test_date_unique(self):
        unique = self.order._meta.get_field('date').unique
        self.assertTrue(unique)

    def test_number_label(self):
        field_label = self.order._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'Ваш номер')

    def test_number_max_length(self):
        max_length = self.order._meta.get_field('number').max_length
        self.assertEquals(max_length, 20)

from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModel(TestCase):

    def test_done_default_false(self):
        item = Item.objects.create(name='Item default false test')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test todo item')
        self.assertEqual(str(item), 'Test todo item')

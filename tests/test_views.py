from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient
        self.menu_data = {'title': 'Menu 1', 'price': 10.99, 'inventory': 5}
        self.menu = Menu.objects.create(**self.menu_data)
        
    def test_getall(self):
        url = reverse('menu_list')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, viewsets
from rest_framework import permissions




from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
class MenuItemView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated] 
    
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated] 
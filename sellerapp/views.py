from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from productapp.models import *
from productapp.serializers import *

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    
from rest_framework import serializers
from .models import *

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_Images
        fields = '__all__'


class ProductFeatureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_Features
        fields = '__all__'


class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_Category
        fields = '__all__'


class ProductCatalogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_Catalog
        fields = '__all__'

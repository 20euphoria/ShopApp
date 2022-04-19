from rest_framework import serializers
from .models import *

class SellerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SellerBankDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seller_Bank_Details
        fields = '__all__'


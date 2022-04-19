from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = [
        'seller_id',
        'user_id',
        'shop_name',
        'shop_address_line1',
        'shop_address_line2',
        'shop_state',
        'shop_city',
        'shop_pincode',
        'shop_mobile_number',
        'shop_mail_id',
        'shop_gstin_number',
        'pan_card_number',
    ]


@admin.register(Seller_Bank_Details)
class SellerBankAdmin(admin.ModelAdmin):
    list_display = [
        'seller_bank_details_id',
        'seller_id',
        'bank_name',
        'bank_branch_name',
        'account_number',
        'ifsc_code',
    ]

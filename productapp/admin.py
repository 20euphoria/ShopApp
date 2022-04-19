from django.contrib import admin
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'company_name', 'company_address', 'company_state', 'company_city',
                    'company_pincode', 'company_gst_number', 'company_registration_number']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'company_id', 'product_name', 'product_quantity', 'product_barcode',
                    'product_description']


@admin.register(Product_Images)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['product_images_id', 'product_id', 'product_image']


@admin.register(Product_Features)
class ProductFeaturesAdmin(admin.ModelAdmin):
    list_display = ['product_features_id', 'product_id',
                    'product_features_name', 'product_features_value']


@admin.register(Product_Category)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product_category_id', 'product_id',
                    'product_category_name', 'product_parent_category']


@admin.register(Product_Catalog)
class ProductCatelogAdmin(admin.ModelAdmin):
    list_display = [
        'product_catalog_id',
        'product_id',
        'seller_id',
        'product_catalog_stock',
        'product_catalog_price',
    ]


@admin.register(Questions)
class QuestionsCategoryAdmin(admin.ModelAdmin):
    list_display = ['questions_id', 'product_id',
                    'questions', 'answers']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'product_id',
                    'review_stars', 'review_comments']


@admin.register(Review_Images)
class ReviewImagesAdmin(admin.ModelAdmin):
    list_display = [
        'review_images_id',
        'review_id',
        'product_review_images',
    ]

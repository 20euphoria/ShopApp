from django.db import models
from sellerapp.models import Seller
from django.contrib.auth.models import User


STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu',
     'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry')
)

PRODUCT_CATEGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('Fashion', 'Fashion'),
    ('Home Appliances', 'Home Appliances'),
    ('Sports', 'Sports'),
    ('Groceries', 'Groceries')
)


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(unique=True, max_length=50)
    company_address = models.CharField(max_length=50)
    company_state = models.CharField(choices=STATE_CHOICES, max_length=50)
    company_city = models.CharField(max_length=50)
    company_pincode = models.IntegerField()
    company_gst_number = models.CharField(max_length=50)
    company_registration_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.company_id},{self.company_name}"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_quantity = models.IntegerField()
    product_barcode = models.CharField(max_length=12, unique=True)
    product_description = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_id},{self.product_name}"


class Product_Images(models.Model):
    product_images_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.FileField(upload_to='product_images')


class Product_Features(models.Model):
    product_features_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_features_name = models.CharField(max_length=50)
    product_features_value = models.CharField(max_length=50)


class Product_Category(models.Model):
    product_category_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_category_name = models.CharField(max_length=50)
    product_parent_category = models.CharField(
        choices=PRODUCT_CATEGORY_CHOICES, max_length=50)


class Product_Catalog(models.Model):
    product_catalog_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_catalog_stock = models.IntegerField()
    product_catalog_price = models.FloatField()


class Questions(models.Model):
    questions_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    questions = models.CharField(max_length=100)
    answers = models.CharField(max_length=100)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_stars = models.IntegerField(null=True)
    review_comments = models.CharField(max_length=50)


class Review_Images(models.Model):
    review_images_id = models.AutoField(primary_key=True)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    product_review_images = models.FileField(
        upload_to='media/product_review_images', null=True)

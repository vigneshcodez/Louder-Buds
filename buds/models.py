from django.db import models
import datetime
import os
from django_summernote.fields import SummernoteTextField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)


class Category(models.Model):
    category_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=False, blank=False)
    category_description = models.TextField(
        max_length=500, null=False, blank=False)
    category_status = models.BooleanField(
        default=False, help_text="0-Show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


class Product_article(models.Model):
    catregory = models.ForeignKey(Category, on_delete=models.CASCADE)
    Product_brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    Product_description = models.TextField(
        max_length=500, null=False, blank=False)
    postimage = models.ImageField(
        upload_to=getFileName, null=False, blank=False)
    content = RichTextField(blank=True, null=True)
    price = models.CharField(max_length=5, null=True, blank=True)
    product_boxitems = models.CharField(max_length=255, null=True, blank=True)
    product_warrenty = models.CharField(max_length=255, null=True, blank=True)
    product_playtime = models.CharField(max_length=255, null=True, blank=True)
    product_waterresistent = models.CharField(
        max_length=255, null=True, blank=True)
    product_fastcharging = models.CharField(
        max_length=255, null=True, blank=True)
    product_buildquality = models.CharField(
        max_length=255, null=True, blank=True)
    product_colours = models.CharField(max_length=255, null=True, blank=True)
    product_mic = models.CharField(max_length=255, null=True, blank=True)
    product_bass_rating = models.FloatField(null=True, blank=True)
    product_build_quality_rating = models.FloatField(null=True, blank=True)
    product_bluetooth_connectivity_rating = models.FloatField(
        null=True, blank=True)

    louderbud_rating = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bestbuy = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product_name


class comparision(models.Model):
    comparision_post_name = models.CharField(
        max_length=255, null=True, blank=True)
    product1_name = models.CharField(max_length=50, null=True, blank=True)
    product1_image = models.ImageField(
        upload_to=getFileName, null=True, blank=True)
    product1_price = models.IntegerField(null=True, blank=True)
    product1_boxitems = models.CharField(max_length=255, null=True, blank=True)
    product1_warrenty = models.CharField(max_length=255, null=True, blank=True)
    product1_playtime = models.CharField(max_length=255, null=True, blank=True)
    product1_waterresistent = models.CharField(
        max_length=255, null=True, blank=True)
    product1_fastcharging = models.CharField(
        max_length=255, null=True, blank=True)
    product1_buildquality = models.CharField(
        max_length=255, null=True, blank=True)
    product1_colours = models.CharField(max_length=255, null=True, blank=True)
    product1_mic = models.CharField(max_length=255, null=True, blank=True)
    product1_bass_rating = models.FloatField(null=True, blank=True)
    product1_build_quality_rating = models.FloatField(null=True, blank=True)
    product1_bluetooth_connectivity_rating = models.FloatField(
        null=True, blank=True)
    product1_louderbud_rating = models.FloatField(null=True, blank=True)

    product2_name = models.CharField(max_length=50, null=True, blank=True)
    product2_image = models.ImageField(
        upload_to=getFileName, null=True, blank=True)
    product2_price = models.IntegerField(null=True, blank=True)
    product2_boxitems = models.CharField(max_length=255, null=True, blank=True)
    product2_warrenty = models.CharField(max_length=255, null=True, blank=True)
    product2_playtime = models.CharField(max_length=255, null=True, blank=True)
    product2_waterresistent = models.CharField(
        max_length=255, null=True, blank=True)
    product2_fastcharging = models.CharField(
        max_length=255, null=True, blank=True)
    product2_buildquality = models.CharField(
        max_length=255, null=True, blank=True)
    product2_colours = models.CharField(max_length=255, null=True, blank=True)
    product2_mic = models.CharField(max_length=255, null=True, blank=True)
    product2_bass_rating = models.FloatField(null=True, blank=True)
    product2_build_quality_rating = models.FloatField(null=True, blank=True)
    product2_bluetooth_connectivity_rating = models.FloatField(
        null=True, blank=True)
    product2_louderbud_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.comparision_post_name

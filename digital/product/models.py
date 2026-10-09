import random
import os
from django.db import models


class Category(models.Model):
    title = models.CharField("title", max_length=20)
    is_enable = models.BooleanField("is_enable", blank=True)
    parent = models.ForeignKey("self", verbose_name="parent", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField("title", max_length=20)
    description = models.TextField("description", max_length=1000, blank=True)
    created_time = models.TimeField("created time", auto_now_add=True)
    updated_time = models.TimeField("updated time", auto_now=True)
    avatar = models.ImageField("avatar", upload_to='products/', blank=True)
    is_enable = models.BooleanField("is enable", default=True)
    categories = models.ManyToManyField("Category", verbose_name="categories", related_name="products")

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_TEXT = 2
    FILE_VIDEO = 3
    FILE_TYPES = ((FILE_VIDEO, 'video'), (FILE_AUDIO, 'audio'), (FILE_TEXT, 'text'))
    file_type = models.PositiveIntegerField('file_type', choices=FILE_TYPES, default=2)
    title = models.CharField("title", )
    created_time = models.TimeField("created time", auto_now_add=True)
    updated_time = models.TimeField("updated time", auto_now=True)

    is_enable = models.BooleanField("is enable", default=True)
    product = models.ForeignKey("Product", verbose_name='product', on_delete=models.CASCADE, related_name='files')
    file = models.FileField("file", upload_to='static/files/%y/%m/%d', blank=True)

    class Meta:
        db_table = "files"
        verbose_name = "File"
        verbose_name_plural = "Files"

    def __str__(self):
        return self.title


class Code(models.Model):
    phone = models.CharField(max_length=15)
    code = models.CharField(max_length=4)
    created = models.DateTimeField(auto_now_add=True)

    def generate_code(self):
        self.code = str(random.randint(1000, 9999))
        self.save()
        return self.code
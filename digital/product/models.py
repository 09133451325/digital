from django.db import models

class Category(models.Model):
    title = models.CharField("title", max_length=20)
    is_enable = models.BooleanField("is_enable", blank=True)
    parent = models.ForeignKey("self", verbose_name="parent", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField("title", max_length=20)
    description = models.TextField("description", max_length=1000, blank=True)
    created_time = models.TimeField("created time", auto_now_add=True)
    updated_time = models.TimeField("updated time", auto_now=True)
    avatar = models.ImageField("avatar", upload_to='products/', blank=True)
    is_enable = models.BooleanField("is enable", default=True)
    categories = models.ManyToManyField("Category", verbose_name="categories")

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"


class File(models.Model):
    title = models.CharField("title", max_length=20)
    created_time = models.TimeField("created time", auto_now_add=True)
    updated_time = models.TimeField("updated time", auto_now=True)
    # avatar = models.ImageField("avatar", upload_to='file/', blank=True)
    is_enable = models.BooleanField("is enable", default=True)
    product = models.ForeignKey("Product", verbose_name='product')
    file = models.FileField("file", upload_to='files/%y/%m/%d', blank=True)

    class Meta:
        db_table = "files"
        verbose_name = "File"
        verbose_name_plural = "Files"

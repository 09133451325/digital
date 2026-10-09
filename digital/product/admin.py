from django.contrib import admin
from .models import Category, Product, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'parent']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']


class FileAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file_type', 'is_enable', 'file']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'is_enable', 'created_time', 'get_file_types']
    list_filter = ['is_enable']
    search_fields = ['title']
    inlines = [FileAdmin]
    filter_horizontal = ["categories"]

    def get_file_types(self, obj):
        result = []
        for file in obj.files.all():
            result.append(file.get_file_type_display())
        return result

    #   return ", ".join(
    #         [file.get_file_type_display() for file in obj.files.all()]
    #   )










from rest_framework import serializers
from .models import Category, File, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField

    class Meta:
        model = File
        fields = ['title', 'file', 'file_type']

        def get_file_type(self, obj):
            return obj.get_fiel_type_display()


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'avatar', 'description', 'categories', 'files']



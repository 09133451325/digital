from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from .models import Category, Product, File, Code
from .serializers import CategorySerializer, ProductSerializer, FileSerializer


def gallery(request):
       categories = Category.objects.prefetch_related('products').all()
       return render(request, 'gallery.html', {'categories': categories})


def product_list(request):
        products = Product.objects.all()
        categories = Category.objects.all()
        files = File.objects.all()
        context = {'products': products,
                   'categories': categories,
                   'files': files}
        return render(request,'home.html', context)


def product_detail(request, pk):

    product= get_object_or_404(Product, pk=pk)
    files = File.objects.filter(product=product)

    context= {'products': product, 'files': files}
    return render(request, 'one.html', context)

################################################
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        context={'categories':categories}
        return Response(request,context)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            categories = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


class FileListView(APIView):
    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):
    def get(self, request, product_id, pk):
        try:
            files = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)

#######################

class SendCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user, created = Code.objects.create()
        code = user.generate_code()
        print("Code:", code)

        return Response({"message":"کد ارسال شد"})
class VerifyCodeView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        code = request.data.get("code")

        try:
            code_user = Code.Object.get(code = code)
        except Code.DoesNotExist:
            return Response({"error":"کد اشتباه است"})
        user, created = Code.objects.get_or_create(phone=phone)
        login(request, user)
        code_user.delete()
        return Response({"message":"ورود موفق"})

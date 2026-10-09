from django.urls import path
from .views import product_list, product_detail,\
    FileListView, FileDetailView, CategoryDetailView,\
    CategoryListView, SendCodeView, VerifyCodeView
app_name = 'root'
urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:product_id>/files/', FileListView.as_view(), name='file_list'),
    path('products/<int:product_id>/files/<int:pk>/', FileDetailView().as_view(), name='file_detail'),
    path("send-otp/", SendCodeView.as_view()),
    path("verify-otp/", VerifyCodeView.as_view()),
]
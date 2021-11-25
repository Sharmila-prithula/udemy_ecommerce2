from django.urls import path
from base.views import product_views as views
from base.views.product_views import *

urlpatterns = [

    path('', views.getProducts, name="products"),

    path('create/', views.createProduct, name="product-create"),
    # path('upload/', views.uploadImage, name="image-upload"),

    # path('<str:pk>/reviews/', views.createProductReview, name="create-review"),
    # path('top/', views.getTopProducts, name='top-products'),
    path('category/', getCategorys.as_view(), name="categorys"),
    path('<str:pk>/', views.getProduct, name="product"),
    path('category/<str:pk>/', views.getCategory, name="category"),

    path('update/<str:pk>/', views.updateProduct, name="product-update"),
    path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),
]
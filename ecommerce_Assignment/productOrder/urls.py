# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()
router.register('products', ProductView, 'products')
router.register('customer', CustomerView, 'customer')
router.register('order', OrderView, 'order')



urlpatterns = [
    # path('products/', ProductView.as_view()),

    path('', include(router.urls)),
]
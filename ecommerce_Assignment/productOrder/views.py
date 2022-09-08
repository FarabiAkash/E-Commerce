# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.files.base import ContentFile
from rest_framework import filters

import uuid
import base64
import os

from ecommerce_Assignment.settings import MEDIA_ROOT
from .models import *
from .serializers import *

# Create your views here.




# Product ViewSet
class ProductView(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def create(self, request):
        user_role = request.GET.get('user_role')
        data_list=request.data
        if user_role=='admin':
            query = Product(name= data_list['name'], stock= data_list['stock'], price=data_list['price'])
            query.save()
            directory = str(uuid.uuid4())
            for i in data_list['product_image']:
                format, imgstr = i.split(';base64,')
                ext = format.split('/')[-1]
                data_image = ContentFile(base64.b64decode(imgstr), name=directory + '.' + ext)
                temp = ProductImage(image=data_image)
                temp.save()
                query.product_image.add(temp)

            return Response({'msg':'Data Posted'})
        else:
            return Response({'msg':'Unauthorized access'})


# PUT request
    def update(self, request, pk=None):         
        data_list=request.data
        user_role = request.GET.get('user_role')
        if user_role=='admin':
            query = Product.objects.get(id=pk)
            query.name= data_list['name']
            query.stock= data_list['stock']
            query.price= data_list['price']
            query.save()
            directory = str(uuid.uuid4())
            path = os.path.join(MEDIA_ROOT, directory)


            for i in data_list['product_image']:
                format, imgstr = i.split(';base64,')
                ext = format.split('/')[-1]
                data_image = ContentFile(base64.b64decode(imgstr), name=directory + '.' + ext)
                temp = ProductImage(image=data_image)
                temp.save()
                query.product_image.add(temp)

            return Response({'msg':'Data Updated'})
        else:
            return Response({'msg':'Unauthorized access'})


# DELETE request
    def destroy(self, request, pk=None):

        user_role = request.GET.get('user_role')
        if user_role=='admin':
            Product.objects.get(id=pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'msg':'Unauthorized access'})


        return Response(status=status.HTTP_204_NO_CONTENT)




# Customer ViewSet
class CustomerView(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers





# Customer ViewSet
class OrderView(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def create(self, request):

        data_list=request.data
        queryCustomer = Customer.objects.get(id=data_list['customer'])
        queryOrder = Order(customer= queryCustomer)
        queryOrder.save()
        for order in data_list['orders']:
            queryProduct = Product.objects.get(id=order['product'])
            queryOrderItem = OrderItem(order= queryOrder, product= queryProduct, quantity=order['quantity'], total_price=(queryProduct.price*order['quantity']))
            queryOrderItem.save()

        return Response({'msg':'Data Posted'})




from rest_framework import serializers
from .models import *


class ProductImageSerializers(serializers.ModelSerializer):
	class Meta:
		model = ProductImage
		fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
	product_image=ProductImageSerializers(many=True)
	class Meta:
		model = Product
		fields = '__all__'
		# depth = 1
                                                                                                                           

class CustomerSerializers(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'

	


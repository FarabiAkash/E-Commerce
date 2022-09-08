from django.db import models

# Create your models here.



class ProductImage(models.Model):
	image = models.ImageField(upload_to='path__product_image', default=0, blank=True)


class Product(models.Model):

	name = models.CharField(max_length=100)
	stock = models.IntegerField(default=0, blank=True)
	price = models.IntegerField(default=0, blank=True)
	product_image = models.ManyToManyField(ProductImage, blank=True)

	def __str__(self):
		return self.name	



status_choice = [
	('delivered', 'delivered'),
	('returned', 'returned'),
	('pending', 'pending'),
]


class Customer(models.Model):
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100, default='customer')
	def __str__(self):
		return self.name	


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	created_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(
		max_length=200, choices=status_choice, blank=False, null=False, default='pending'
		) 


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
	product = models.ForeignKey(Product, on_delete=models.PROTECT)
	quantity = models.PositiveIntegerField(default=1)
	total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
from django.db import models

class Customer (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    date_registration = models.DateField()

    def __str__(self):
        return f'Customer: {self.name}, email: {self.email}, address {self.address}, date of reg: {self.date_registration}'


class Product (models.Model):
    name_product = models.CharField(max_length=70)
    desctiption = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = models.IntegerField()
    date_upload = models.DateTimeField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
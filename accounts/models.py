from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField(default='profile.png',null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    # it gives how the actually file look like
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        )

    name = models.CharField(max_length=200)
    price= models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True, choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(max_length=200,null=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS =(
        ('Pending', 'Pending'),
        ('Out for delivery','out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET, null=True)
    status = models.CharField(max_length=200,null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    note = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.product.name

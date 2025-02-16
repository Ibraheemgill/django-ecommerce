from django.db import models

# Create your models here.
class Collection(models.Model):
    title=models.CharField(max_length=255)
    featured_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')

class Promotion(models.Model):
    description=models.CharField(max_length=255)
    discount=models.FloatField()
    #products



class Product(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    title=models.CharField(max_length=50,default="")
    description=models.TextField(default='')
    unit_price=models.DecimalField(default='',max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateField(auto_now=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotion=models.ManyToManyField(Promotion)
    slug=models.SlugField(default="")




class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD ='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    first_name=models.CharField(max_length=50,default="")
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    dob=models.DateField(null=True)
    memberShip=models.CharField(max_length=1,default=MEMBERSHIP_BRONZE,choices=MEMBERSHIP_CHOICES)
   

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    PAYMENT_STATUS_PENDING='P'
    PAYMENT_STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED='F'
    PAYMENT_STATUS_OPTION=[
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed'),
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS_OPTION,default=PAYMENT_STATUS_PENDING)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

class OrderItem(models.Model):
    
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=8,decimal_places=2)

class cart_item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()

class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    # customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)


from django.db import models

# Create your models here.

class Catogory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    catogory = models.ForeignKey(Catogory, on_delete=models.CASCADE, default='',null=True, blank=True)
    desc = models.TextField(default='')
    image = models.ImageField(upload_to ='uploads/products', default= '', null=True, blank=True)

    @staticmethod
    def get_all_products_by_id(catogory_id):
        if catogory_id:
            return Products.objects.filter(catogory=catogory_id)
        else:
            return Products.objects.all()



class Customers(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15, default='')
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def register(self):
        self.save()

    @staticmethod
    def getcustomer_by_email(email):
        try:
            return Customers.objects.get(email=email)
        except:
            return False

        

    def isExists(self):
        try:
            return Customers.objects.get(email =self.email)
        except:
            return False


        

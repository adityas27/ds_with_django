from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120, help_text="name of product")
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text="In Indian Rupees ₹")
    created = models.DateTimeField(auto_now_add=True, help_text="Date when created")
    updated = models.DateTimeField(auto_now=True, help_text="Date when updated")

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"
    

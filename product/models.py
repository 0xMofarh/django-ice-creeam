from django.db import models

class Product(models.Model):
    
    name = models.CharField(max_length=100, blank=True ,null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True ,null=True)
    contact = models.TextField(blank=True ,null=True)
    img = models.ImageField(upload_to='images/%y/%m/%d', blank=True ,null=True)
    active = models.BooleanField(default=False)
    activetoday = models.BooleanField(default=False)
    category = models.CharField(max_length=50, blank=True, null=True, choices=[('بسكوت','بسكوت'),('كوب','كوب'),('مشروب','مشروب')])
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'

from django.db import models

class Work(models.Model):
    
    title = models.CharField(max_length=100, blank=True ,null=True)
    contact = models.TextField(blank=True ,null=True)
    img = models.ImageField(upload_to='work/%y/%m/%d', blank=True ,null=True)
    active = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Work'


class Info(models.Model):
    
    title = models.CharField(max_length=100, blank=True ,null=True)
    contact = models.TextField(blank=True ,null=True)
    img = models.ImageField(upload_to='icons/%y/%m/%d', blank=True ,null=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'info'


class Carousel(models.Model):
    
    img = models.ImageField(upload_to='Carousel/%y/%m/%d', blank=True ,null=True)
    
    class Meta:
        verbose_name = 'Carousel'
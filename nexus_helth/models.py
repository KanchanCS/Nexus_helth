from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models .CharField(max_length=50) 
    email=models.EmailField(max_length=100) 
    phone=models.CharField(max_length=15)
    message=models.TextField()
    

class Banner(models.Model):
# sub_head main_heading banner_img sub_text 
 sub_head=models.CharField(max_length=100)
 main_heading=models.CharField(max_length=100)
 banner_img= models.ImageField(upload_to='images/') 
 sub_text=models.TextField()

class User(models.Model):
    customer_name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    feedback=models.TextField()

class AppointmentBook(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=12)
    requirements=models.TextField()
    week_days = models.CharField(
        max_length=225,
        null=True,
        blank=True
    )
   
    
   
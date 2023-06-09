from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    registration_number = models.CharField( max_length=50)  
    profile_pic = models.ImageField(upload_to='profile_pic/student/', null=True, blank=True)  
    address = models.CharField( max_length=150)
    mobile = models.CharField(max_length=10, null=False)

    @property
    def get_name(self):
        return self.user.first_name +" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


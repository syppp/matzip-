from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField()
    email = models.TextField()
    phone_num = models.TextField()
    school = models.TextField()


class Inputform(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)    
    title = models.TextField()
    product_name = models.TextField()
    location = models.TextField()
    person_num = models.TextField()
    price = models.TextField()
    link = models.TextField()
    account = models.TextField()
    date_limit = models.DateTimeField('date published')
    explanation = models.CharField(max_length=300)
    photo = models.FileField(upload_to='inputphotos/', blank=True, null=True) #blank랑 null 둘 다 써도 되나?




    

from django.db import models
from accounts.models import Inputform 

# Create your models here.

class Comment(models.Model):   
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.TextField(max_length=20)
    comment_textfield = models.TextField()
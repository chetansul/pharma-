from django.db import models
from django.contrib.auth.models import User
#from core.models import drugs
import uuid
# Create your models here. 
class profile(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True) 
    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=500,blank=True,null=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to="core/profiles/",)
    user_id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.user.username)
    
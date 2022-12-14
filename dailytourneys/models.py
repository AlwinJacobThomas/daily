from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class BGMI(models.Model):

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    price = models.IntegerField(null=True)


def __str__(self):
    return self.name

class CustomAccountManager(BaseUserManager):

 def create_superuser(self,email,username,first_name,password, **other_fields):

  other_fields.setdefault('is_staff',True)
  other_fields.setdefault('is_superuser',True)
  other_fields.setdefault('is_active',True)

  if other_fields.get ('is_staff') is not True:
   raise ValueError('super user not staff=True')


  if other_fields.get ('is_superuser') is not True:
   raise ValueError('super user not superuser=True')
  return self.create_user(email,username,first_name,password,**other_fields)

 #def create_user(self,email,username,first_name,password,orgname,about,**other_fields):
  
  if not username:
            raise ValueError("Unique username is required")
  if not email:
            raise ValueError("User must have an email address")
  if not password:
            raise ValueError("Password is required")
      
  email = self.normalize_email(email)
  user = self.model(email = email,username = username,first_name = first_name, **other_fields)
  user.set_password(password)
  user.orgname = orgname
  user.about = about
  user.save()

  return user
  

class NewUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    orgname = models.CharField(max_length=50)
    start_date = models.DateTimeField(default = timezone.now)
    about = models.TextField(('about'),max_length=500,blank = True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','password']

    def __str__(self):
      return self.username
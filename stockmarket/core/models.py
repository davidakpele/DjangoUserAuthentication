# models.py
from django.db import models
from db_connection import db
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your model here
User = get_user_model()
user_collection = db['users']
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class Trader(models.Model):
    id_user = models.IntegerField()
    name = models.CharField(max_length=100, blank=True) 
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)

class Transaction(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField()

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    firstname = models.CharField(max_length=100, blank=True) 
    lastname = models.CharField(max_length=100, blank=True)
    age = models.CharField(max_length=80, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = UserManager()

    def __str__(self):
        return self.email
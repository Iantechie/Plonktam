from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
      if not email:
          raise ValueError("Enter a valid email")
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)

      return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff should be set to True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser should be set to True')
        
        return self._create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    phone_number = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = None
    groups = None
    user_permissions = None
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
class CoverDetails(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    create_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
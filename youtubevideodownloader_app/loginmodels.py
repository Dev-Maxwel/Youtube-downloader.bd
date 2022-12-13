from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, ** extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        if not password:
            raise ValueError("Password is required")
        
        user = self,model(
            email = self.normalize_email(email),
            user_name = first_name,
            **extra_fields

        )
        
        user.set_password(password)
        user.save(using=self_db)
        return user
    
    def create_user(self, email, password, username, **extrafield):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, username, **extra_fields)
        
    def create_superuser(self, email, password, username, **extrafield):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, username, **extra_fields)
        

class User(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(max_length=300, unique=True, db_index=True) 
    username= models.CharField(max_length=100) 
    password= models.CharField(max_length=300) 
   
    
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'username', 'password']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    




















from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Creamos una clase que tenga las opraciones que me permitan crear un nueva usuario y superusuario
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:    # Si no tiene email que lanse un error raise
            raise ValueError('el usuario debe tener un email')
        
        if not username:
            raise ValueError('el usuario debe tener un username')
        
        # definimos un objeto de tipo user
        user= self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # Creamos una función que nos permita crear un superusuario
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    


# Creamos la clase account
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)    # Este campo va a ser unico
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    
    # Declaramos los campos por defecto que tiene django
    date_joined = models.DateTimeField(auto_now_add=True)    # Fecha de inicio sesión
    last_login = models.DateTimeField(auto_now_add=True)    # Si ha iniciado sesión
    is_admin = models.BooleanField(default=False)    # Es administrado? por defecto es false
    is_staff = models.BooleanField(default=False)    # Si es parte de la plataforma staff
    is_active = models.BooleanField(default=False)    # Si esta activo
    is_superadmin = models.BooleanField(default=False)    # Si es administrador
    
    # El usuario para iniciar sesion debe utilizar el email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']   # Campos requeridos para el formulario de registro
    
    objects = MyAccountManager()
    
    # Listamos por defecto un label
    def __str__(self):
        return self.email
    
    # Declaramos otra función para identificar si tiene permisos
    def has_perm(self, perm, obj=None):
        return self.is_admin    # Solo si es admin puede hacer modificaciones
    
    def has_module_perms(self, add_label):
        return True
    